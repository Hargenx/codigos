import React, { useEffect } from "react";
import { NavigationContainer } from "@react-navigation/native";
import AppNavigator from "./src/navigation/AppNavigator";
import Realm from "realm"; // Import Realm
import { getRealm } from "./src/realm/realmConfig"; // Import getRealm

const App = () => {
  // Opcional: Gerenciar uma instância global do Realm aqui ou fechar ao sair do app.
  // Para este exemplo, cada tela gerencia sua necessidade de Realm,
  // mas para apps maiores, um RealmProvider com Context API pode ser melhor.

  let realmInstance: Realm | null = null;

  useEffect(() => {
    const initialize = async () => {
      try {
        // Opcional: Abrir uma instância aqui se for usá-la globalmente
        // realmInstance = await getRealm();
        // console.log("Realm inicializado globalmente no App.tsx (opcional)");
      } catch (error) {
        console.error(
          "Falha ao inicializar Realm globalmente no App.tsx:",
          error
        );
      }
    };

    initialize();

    return () => {
      // Fechar a instância global do Realm se ela foi aberta aqui
      // if (realmInstance && !realmInstance.isClosed) {
      //   console.log("Fechando Realm global do App.tsx");
      //   realmInstance.close();
      // }
    };
  }, []);

  return (
    <NavigationContainer>
      <AppNavigator />
    </NavigationContainer>
  );
};

export default App;
