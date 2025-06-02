import React, { useContext, useCallback } from 'react';
import { FlatList, TouchableOpacity } from 'react-native';
import styled from 'styled-components/native';
import Icon from 'react-native-vector-icons/MaterialIcons';
import { GameContext } from '../context/GameContext';
import { deleteGame, initDB } from '../database/baseDados';
import { useNavigation } from '@react-navigation/native';
import { Game } from '../types/Game';

export default function GameListScreen(): JSX.Element {
    const { games, reload } = useContext(GameContext);
    const navigation = useNavigation();

    const handleDelete = async (id) => {
        await deleteGame(id);
        reload();
    };

    const renderItem = useCallback(({ item }: { item: Game }) => (
        <ItemRow>
        <TouchableOpacity onPress= {() => navigation.navigate('Details', { game: item })
}>
    <ItemText>{ item.title } </ItemText>
    </TouchableOpacity>
    < Icons >
    <Icon name="edit" size = { 24} onPress = {() => navigation.navigate('EditGame', { gameId: item.id })} />
        < Icon name = "delete" size = { 24} onPress = {() => handleDelete(item.id)} />
            </Icons>
            </ItemRow>
  ), []);

return (
    <Container>
    <FlatList
        data= { games }
keyExtractor = {(item) => String(item.id)}
renderItem = { renderItem }
contentContainerStyle = {{ padding: 16 }}
      />
    < AddButton onPress = {() => navigation.navigate('AddGame')}>
        <Icon name="add" size = { 32} color = "#fff" />
            </AddButton>
            </Container>
  );
}

const Container = styled.View`flex: 1;`;
const ItemRow = styled.View`
  flex-direction: row;
  justify-content: space-between;
  padding: 12px;
  border-bottom-width: 1px;
  border-color: #eee;
`;
const ItemText = styled.Text`font-size: 16px;`;
const Icons = styled.View`flex-direction: row; width: 72px; justify-content: space-between;`;
const AddButton = styled.TouchableOpacity`
  position: absolute;
  bottom: 24px;
  right: 24px;
  background-color: #2196f3;
  padding: 16px;
  border-radius: 32px;
`;