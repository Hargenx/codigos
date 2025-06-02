import React, { createContext, useState, useEffect, ReactNode } from "react";
import { Game } from "../types/Game";
import { initDB, fetchAllGames } from "../database/baseDados";

interface GameContextData {
  games: Game[];
  reload: () => void;
}

export const GameContext = createContext<GameContextData>(
  {} as GameContextData
);

export function GameProvider({ children }: { children: ReactNode }) {
  const [games, setGames] = useState<Game[]>([]);

  function loadGames() {
    fetchAllGames(setGames);
  }

  useEffect(() => {
    initDB();
    loadGames();
  }, []);

  return (
    <GameContext.Provider value={{ games, reload: loadGames }}>
      {children}
    </GameContext.Provider>
  );
}
