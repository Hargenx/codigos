import React, { useContext } from 'react';
import { GameForm } from '../components/GameForm';
import { insertGame, initDB } from '../database/baseDados';
import { GameContext } from '../context/GameContext';
import { useNavigation } from '@react-navigation/native';

export default function AddGameScreen(): JSX.Element {
    const { reload } = useContext(GameContext);
    const navigation = useNavigation();

    const handleAdd = async (game) => {
        await initDB();
        await insertGame(game);
        reload();
        navigation.goBack();
    };

    return <GameForm onSubmit={ handleAdd } />;
}