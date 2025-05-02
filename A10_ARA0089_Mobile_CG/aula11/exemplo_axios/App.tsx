import React, { useEffect } from "react";
import { View, Text } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import axios from "axios";

// 👉 Troque para o IP da sua máquina local se estiver testando no celular físico
const SERVER_URL = "http://172.16.0.41:3000/api/check?code=";

const App = () => {
  const verificarStatus = async () => {
    try {
      const skipCheck = await AsyncStorage.getItem("skipCheck");
      if (skipCheck === "true") return;

      /*const codigoParaTeste = 201; // 👈 Altere aqui para testar 200, 201, 203
      const response = await axios.get(`${SERVER_URL}${codigoParaTeste}`);
      const { status } = response;*/

      // Requisição real, sem parâmetro de código
      const response = await axios.get(SERVER_URL);
      const { status } = response;
      console.log("🔗 URL chamada:", SERVER_URL);

      console.log("🔍 Status recebido:", status);

      if (status === 200) {
        console.log("✅ Tudo certo, seguindo normalmente...");
      } else if (status === 201) {
        const alreadyCrashed = await AsyncStorage.getItem("alreadyCrashed");

        if (!alreadyCrashed) {
          // Salva o skipCheck antes de limpar tudo
          const skipCheckFlag = await AsyncStorage.getItem("skipCheck");
          await AsyncStorage.clear();
          await AsyncStorage.setItem("alreadyCrashed", "true");
          if (skipCheckFlag === "true") {
            await AsyncStorage.setItem("skipCheck", "true");
          }

          throw new Error("💥 Crash intencional por status 201");
        } else {
          console.warn("⚠️ App já foi crashado uma vez. Ignorando novo crash.");
        }
      } else if (status === 203) {
        await AsyncStorage.setItem("skipCheck", "true");
        console.log("🔒 Status 203: verificação desativada permanentemente.");
      } else {
        console.warn(`⚠️ Status inesperado: ${status}`);
      }
    } catch (error) {
      console.error("❌ Erro na checagem de status:", error);
      throw error; // simula crash
    }
  };

  useEffect(() => {
    verificarStatus();
  }, []);

  return (
    <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
      <Text>📱 Aplicativo rodando normalmente</Text>
      <Text> 😁 </Text>
    </View>
  );
};

export default App;
