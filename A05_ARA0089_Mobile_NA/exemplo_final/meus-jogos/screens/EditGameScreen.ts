import React, { useContext, useEffect, useState } from 'react';
import { GameForm } from '../components/GameForm';
import { updateGame } from '../database/baseDados';
import { GameContext } from '../context/GameContext';
import { useNavigation, useRoute } from '@react-navigation/native';
import { Game } from '../types/Game';

export default function EditGameScreen(): JSX.Element {
    const { games, reload } = useContext(GameContext);
    const navigation = useNavigation();
    const route = useRoute();
    const { gameId } = route.params;
    const [game, setGame] = useState<Game>(null);

    useEffect(() => {
        const found = games.find((g) => g.id === gameId);
        setGame(found);
    }, [games]);

    const handleUpdate = async (data: Game) => {
        await updateGame({ ...data, id: gameId });
        reload();
        navigation.goBack();
    };

    return game ? <GameForm defaultValues={ game } onSubmit = { handleUpdate } /> : null;
}