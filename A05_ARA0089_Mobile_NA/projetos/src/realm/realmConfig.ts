import Realm from 'realm';
import { PlayerSchema } from './schemas';

// Configuração para abrir o Realm.
// Em um app real, você pode querer adicionar `schemaVersion` e `migration`
// à medida que seu schema evolui.
const realmConfig: Realm.Configuration = {
    schema: [PlayerSchema],
    // schemaVersion: 1, // Descomente e incremente ao mudar o schema
    // migration: (oldRealm, newRealm) => {
    //   if (oldRealm.schemaVersion < 1) {
    //     // Código de migração aqui
    //   }
    // },
};

// Função para obter a instância do Realm.
// Isso garante que estamos sempre trabalhando com a mesma configuração.
export const getRealm = async () => {
    try {
        return await Realm.open(realmConfig);
    } catch (error) {
        console.error('Falha ao abrir o Realm:', error);
        // Em um app real, trate este erro de forma mais robusta
        // (ex: mostrando uma mensagem para o usuário, tentando novamente)
        throw error; // Re-lança o erro para quem chamou tratar
    }
};