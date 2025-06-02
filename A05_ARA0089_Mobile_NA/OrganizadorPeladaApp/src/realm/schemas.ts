import { ObjectSchema } from 'realm';
import { BSON } from 'realm'; // Necessário se for usar ObjectID diretamente no schema

export const PlayerSchema: ObjectSchema = {
    name: 'Player', // Nome do modelo no Realm
    properties: {
        _id: 'objectId',
        name: 'string',
        position: { type: 'string', default: 'Indefinido' },
        skillLevel: { type: 'int', default: 3 }, // Nível de habilidade (1-5)
        createdAt: { type: 'date', default: () => new Date() },
    },
    primaryKey: '_id',
};