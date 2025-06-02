import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import HomeScreen from "../screens/HomeScreen";
import AddGameScreen from "../screens/AddGameScreen";
import EditGameScreen from "../screens/EditGameScreen";
import GameDetailsScreen from "../screens/GameDetailsScreen";

export type RootStackParamList = {
  Home: undefined;
  AddGame: undefined;
  EditGame: { gameId: number };
  Details: { gameId: number };
};

const Stack = createStackNavigator<RootStackParamList>();

export default function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen
          name="AddGame"
          component={AddGameScreen}
          options={{ title: "Adicionar Jogo" }}
        />
        <Stack.Screen
          name="EditGame"
          component={EditGameScreen}
          options={{ title: "Editar Jogo" }}
        />
        <Stack.Screen
          name="Details"
          component={GameDetailsScreen}
          options={{ title: "Detalhes" }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
