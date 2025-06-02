import React from "react";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import PlayerListScreen from "../screens/PlayerListScreen";
import PlayerFormScreen from "../screens/PlayerFormScreen";
import { Player as PlayerType } from "../types/player"; // Importar Player como PlayerType

// Definindo os tipos para os parâmetros das rotas
export type RootStackParamList = {
  PlayerList: undefined;
  PlayerForm: { playerToEdit?: PlayerType }; // playerToEdit agora é um PlayerType (POJO)
};

const Stack = createNativeStackNavigator<RootStackParamList>();

const AppNavigator = () => {
  return (
    <Stack.Navigator initialRouteName="PlayerList">
      <Stack.Screen
        name="PlayerList"
        component={PlayerListScreen}
        options={{ title: "Jogadores da Pelada" }}
      />
      <Stack.Screen
        name="PlayerForm"
        component={PlayerFormScreen}
        options={({ route }) => ({
          title: route.params?.playerToEdit
            ? "Editar Jogador"
            : "Adicionar Jogador",
        })}
      />
    </Stack.Navigator>
  );
};

export default AppNavigator;
