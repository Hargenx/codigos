import React from "react";
import AppNavigator from "./navigation/AppNavigator";
import { GameProvider } from "./context/GameContext";

export default function App() {
  return (
    <GameProvider>
      <AppNavigator />
    </GameProvider>
  );
}
