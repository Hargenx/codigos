import React from "react";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import PlayerListScreen from "../screens/PlayerListScreen";
import PlayerFormScreen from "../screens/PlayerFormScreen";
import { Player } from "../types/player"; // Importar o tipo Player

// Definindo os tipos para os parâmetros das rotas
export type RootStackParamList = {
  PlayerList: undefined; // Tela PlayerList não recebe parâmetros obrigatórios
  PlayerForm: { playerToEdit?: Player | (Player & Realm.Object) }; // playerToEdit é opcional
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
