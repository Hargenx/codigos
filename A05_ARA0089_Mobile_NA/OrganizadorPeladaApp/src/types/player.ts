import { BSON } from 'realm';

export interface Player {
    _id: BSON.ObjectId;
    name: string;
    position: 'Goleiro' | 'Defensor' | 'Meio-campo' | 'Atacante' | 'Indefinido';
    skillLevel: 1 | 2 | 3 | 4 | 5; // Nível de 1 a 5
    createdAt: Date;
}
