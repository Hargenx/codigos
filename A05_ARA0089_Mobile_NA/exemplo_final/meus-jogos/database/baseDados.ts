import * as SQLite from 'expo-sqlite';
import { Game } from '../types/Game';

// Abre (ou cria) o banco de dados
const db = SQLite.openDatabaseSync('jogos.db');

// Inicializa a tabela de jogos
export async function initDB(): Promise<void> {
    await db.withTransactionAsync(async () => {
        await db.execAsync(`CREATE TABLE IF NOT EXISTS jogos (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT NOT NULL,
         genre TEXT NOT NULL,
         releaseYear INTEGER NOT NULL
       );`);
    });
}

// Busca todos os jogos
export async function fetchAllGames(callback: (games: Game[]) => void): Promise<void> {
    await db.withTransactionAsync(async () => {
        try {
            const result = await db.getAllAsync<Game>('SELECT * FROM jogos;');
            callback(result);
        } catch (error) {
            console.error('Erro ao buscar jogos:', error);
        }
    });
}
export async function insertGame(game: Game, onSuccess: () => void): Promise<void> {
    try {
        await db.withTransactionAsync(async () => {
            await db.runAsync(
                'INSERT INTO jogos (title, genre, releaseYear) VALUES (?, ?, ?);',
                [game.title, game.genre, game.releaseYear]
            );
            onSuccess();
        });
    } catch (error) {
        console.error('Erro ao inserir jogo:', error);
    }
}

// Atualiza um jogo existente
export async function updateGame(game: Game, onSuccess: () => void): Promise<void> {
    if (game.id == null) return;
    try {
        await db.withTransactionAsync(async () => {
            await db.runAsync(
                'UPDATE jogos SET title = ?, genre = ?, releaseYear = ? WHERE id = ?;',
                [game.title, game.genre, game.releaseYear, game.id as number]
            );
            onSuccess();
        });
    } catch (error) {
        console.error('Erro ao atualizar jogo:', error);
    }
}

// Deleta um jogo pelo id
export async function deleteGame(id: number, onSuccess: () => void): Promise<void> {
    try {
        await db.withTransactionAsync(async () => {
            await db.runAsync(
                'DELETE FROM jogos WHERE id = ?;',
                [id]
            );
            onSuccess();
        });
    } catch (error) {
        console.error('Erro ao deletar jogo:', error);
    }
}