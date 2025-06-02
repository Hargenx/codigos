import React, { useState, useCallback, useRef } from "react";
import {
  View,
  Text,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  Alert,
  SafeAreaView,
} from "react-native";
import Realm from "realm";
import { useNavigation, useFocusEffect } from "@react-navigation/native";
import { NativeStackNavigationProp } from "@react-navigation/native-stack";
import { getRealm } from "../realm/realmConfig";
import { Player as PlayerType } from "../types/player"; // Importar Player como PlayerType
import { RootStackParamList } from "../navigation/AppNavigator";

type PlayerListScreenNavigationProp = NativeStackNavigationProp<
  RootStackParamList,
  "PlayerList"
>;

// Tipo para objetos Player gerenciados pelo Realm
type RealmPlayer = PlayerType & Realm.Object<PlayerType>;

const PlayerListScreen = () => {
  const navigation = useNavigation<PlayerListScreenNavigationProp>();
  const [realmInstance, setRealmInstance] = useState<Realm | null>(null);
  const [players, setPlayers] = useState<RealmPlayer[]>([]);
  const playerCollectionRef = useRef<Realm.Results<RealmPlayer> | null>(null);

  const loadPlayers = useCallback(async (currentRealm: Realm) => {
    try {
      const playerObjects = currentRealm
        .objects<PlayerType>("Player")
        .sorted("name") as Realm.Results<RealmPlayer>;
      playerCollectionRef.current = playerObjects;
      setPlayers([...playerObjects]);

      playerObjects.addListener((collection) => {
        setPlayers([...collection]);
      });
    } catch (error) {
      console.error("Falha ao carregar jogadores:", error);
      Alert.alert("Erro", "Não foi possível carregar os jogadores.");
    }
  }, []);

  useFocusEffect(
    useCallback(() => {
      let currentRealm: Realm;
      const initRealm = async () => {
        try {
          currentRealm = await getRealm();
          setRealmInstance(currentRealm);
          await loadPlayers(currentRealm);
        } catch (e) {
          console.error("Erro inicializando Realm em PlayerListScreen", e);
          Alert.alert("Erro", "Não foi possível conectar ao banco de dados.");
        }
      };
      initRealm();

      return () => {
        if (
          playerCollectionRef.current &&
          typeof playerCollectionRef.current.removeAllListeners === "function"
        ) {
          playerCollectionRef.current.removeAllListeners();
        }
      };
    }, [loadPlayers])
  );

  const handleDeletePlayer = useCallback(
    (playerToDelete: RealmPlayer) => {
      if (!realmInstance || realmInstance.isClosed) {
        Alert.alert("Erro", "Banco de dados não está acessível.");
        return;
      }
      Alert.alert(
        "Confirmar Exclusão",
        `Deseja excluir o jogador "${playerToDelete.name}"?`,
        [
          { text: "Cancelar", style: "cancel" },
          {
            text: "Excluir",
            style: "destructive",
            onPress: () => {
              try {
                realmInstance.write(() => {
                  realmInstance.delete(playerToDelete);
                });
              } catch (error) {
                console.error("Falha ao excluir jogador:", error);
                Alert.alert("Erro", "Não foi possível excluir o jogador.");
              }
            },
          },
        ]
      );
    },
    [realmInstance]
  );

  const renderPlayerItem = ({ item }: { item: RealmPlayer }) => (
    <TouchableOpacity
      style={styles.playerItem}
      onPress={() =>
        navigation.navigate("PlayerForm", {
          playerToEdit: item.toJSON() as unknown as PlayerType,
        })
      }
      onLongPress={() => handleDeletePlayer(item)}
    >
      <View style={styles.playerDetailsContainer}>
        <Text style={styles.playerName}>{item.name}</Text>
        <Text style={styles.playerDetails}>Posição: {item.position}</Text>
        <Text style={styles.playerDetails}>
          Habilidade: {item.skillLevel}/5
        </Text>
      </View>
      <TouchableOpacity
        onPress={() => handleDeletePlayer(item)}
        style={styles.deleteButtonSmall}
      >
        <Text style={styles.deleteButtonTextSmall}>X</Text>
      </TouchableOpacity>
    </TouchableOpacity>
  );

  if (!realmInstance) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <Text>Carregando banco de dados...</Text>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <FlatList
        data={players}
        renderItem={renderPlayerItem}
        keyExtractor={(item) => item._id.toHexString()}
        ListEmptyComponent={
          <Text style={styles.emptyText}>Nenhum jogador cadastrado.</Text>
        }
        contentContainerStyle={styles.listContentContainer}
      />
      <TouchableOpacity
        style={styles.addButton}
        onPress={() => navigation.navigate("PlayerForm", {})}
      >
        <Text style={styles.addButtonText}>Adicionar Jogador</Text>
      </TouchableOpacity>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f5f5f5",
  },
  loadingContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  listContentContainer: {
    paddingBottom: 80,
  },
  playerItem: {
    backgroundColor: "#ffffff",
    padding: 15,
    marginVertical: 8,
    marginHorizontal: 16,
    borderRadius: 8,
    elevation: 2,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  playerDetailsContainer: {
    flex: 1,
  },
  playerName: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#333",
  },
  playerDetails: {
    fontSize: 14,
    color: "#666",
    marginTop: 2,
  },
  deleteButtonSmall: {
    padding: 8,
    backgroundColor: "#ff4d4f",
    borderRadius: 20,
    width: 30,
    height: 30,
    justifyContent: "center",
    alignItems: "center",
    marginLeft: 10,
  },
  deleteButtonTextSmall: {
    color: "#fff",
    fontWeight: "bold",
    fontSize: 14,
  },
  addButton: {
    backgroundColor: "#6200ee",
    paddingVertical: 15,
    paddingHorizontal: 20,
    borderRadius: 30,
    position: "absolute",
    bottom: 25,
    right: 25,
    elevation: 5,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
  },
  addButtonText: {
    color: "#ffffff",
    fontSize: 16,
    fontWeight: "bold",
  },
  emptyText: {
    textAlign: "center",
    marginTop: 50,
    fontSize: 18,
    color: "#777",
  },
});

export default PlayerListScreen;
