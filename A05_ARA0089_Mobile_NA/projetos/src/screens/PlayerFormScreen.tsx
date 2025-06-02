import React, { useState, useEffect, useCallback } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  Alert,
  ScrollView,
  SafeAreaView,
} from "react-native";
import Realm, { BSON } from "realm";
import { useNavigation, useRoute, RouteProp } from "@react-navigation/native";
import { NativeStackNavigationProp } from "@react-navigation/native-stack";
import { getRealm } from "../realm/realmConfig";
import { Player as PlayerType } from "../types/player";
import { RootStackParamList } from "../navigation/AppNavigator";

type PlayerFormScreenNavigationProp = NativeStackNavigationProp<
  RootStackParamList,
  "PlayerForm"
>;
type PlayerFormScreenRouteProp = RouteProp<RootStackParamList, "PlayerForm">;

type RealmPlayer = PlayerType & Realm.Object<PlayerType>;

const POSITIONS: PlayerType["position"][] = [
  "Goleiro",
  "Defensor",
  "Meio-campo",
  "Atacante",
  "Indefinido",
];
const SKILL_LEVELS: PlayerType["skillLevel"][] = [1, 2, 3, 4, 5];

const PlayerFormScreen = () => {
  const navigation = useNavigation<PlayerFormScreenNavigationProp>();
  const route = useRoute<PlayerFormScreenRouteProp>();
  const playerToEditFromRoute = route.params?.playerToEdit;

  const [realmInstance, setRealmInstance] = useState<Realm | null>(null);
  const [name, setName] = useState(playerToEditFromRoute?.name || "");
  const [position, setPosition] = useState<PlayerType["position"]>(
    playerToEditFromRoute?.position || "Indefinido"
  );
  const [skillLevel, setSkillLevel] = useState<PlayerType["skillLevel"]>(
    playerToEditFromRoute?.skillLevel || 3
  );
  const [editingId, setEditingId] = useState<BSON.ObjectId | null>(null);

  useEffect(() => {
    const initRealm = async () => {
      try {
        const realm = await getRealm();
        setRealmInstance(realm);
      } catch (e) {
        console.error("Erro inicializando Realm em PlayerFormScreen", e);
        Alert.alert("Erro", "Não foi possível conectar ao banco de dados.");
        navigation.goBack();
      }
    };
    initRealm();

    if (playerToEditFromRoute?._id) {
      // Certifica que _id é um BSON.ObjectId. O método toJSON() deve preservar isso.
      // Se vier como string, precisa ser convertido: new BSON.ObjectId(playerToEditFromRoute._id as string)
      // Assumindo que toJSON() mantém o tipo ou que o _id na PlayerType é sempre ObjectId
      setEditingId(playerToEditFromRoute._id as BSON.ObjectId);
    }
  }, [navigation, playerToEditFromRoute]);

  const handleSavePlayer = useCallback(async () => {
    if (!realmInstance || realmInstance.isClosed) {
      Alert.alert("Erro", "Banco de dados não está pronto ou está fechado.");
      return;
    }
    if (name.trim() === "") {
      Alert.alert("Atenção", "O nome do jogador é obrigatório.");
      return;
    }

    try {
      realmInstance.write(() => {
        if (editingId) {
          const playerInRealm = realmInstance.objectForPrimaryKey<PlayerType>(
            "Player",
            editingId
          ) as RealmPlayer | null;
          if (playerInRealm) {
            playerInRealm.name = name.trim();
            playerInRealm.position = position;
            playerInRealm.skillLevel = skillLevel;
          } else {
            Alert.alert("Erro", "Jogador não encontrado para edição.");
            return;
          }
        } else {
          realmInstance.create<PlayerType>("Player", {
            _id: new BSON.ObjectId(),
            name: name.trim(),
            position,
            skillLevel,
            createdAt: new Date(),
          });
        }
      });
      navigation.goBack();
    } catch (error) {
      console.error("Falha ao salvar jogador:", error);
      Alert.alert("Erro", "Não foi possível salvar o jogador.");
    }
  }, [realmInstance, name, position, skillLevel, editingId, navigation]);

  const renderPositionSelector = () => (
    <View style={styles.selectorContainer}>
      <Text style={styles.label}>Posição:</Text>
      <View style={styles.optionsContainer}>
        {POSITIONS.map((pos) => (
          <TouchableOpacity
            key={pos}
            style={[
              styles.optionButton,
              position === pos && styles.optionButtonSelected,
            ]}
            onPress={() => setPosition(pos)}
          >
            <Text
              style={[
                styles.optionButtonText,
                position === pos && styles.optionButtonTextSelected,
              ]}
            >
              {pos}
            </Text>
          </TouchableOpacity>
        ))}
      </View>
    </View>
  );

  const renderSkillSelector = () => (
    <View style={styles.selectorContainer}>
      <Text style={styles.label}>Nível de Habilidade (1-5):</Text>
      <View style={styles.optionsContainer}>
        {SKILL_LEVELS.map((lvl) => (
          <TouchableOpacity
            key={lvl}
            style={[
              styles.optionButton,
              styles.skillButton,
              skillLevel === lvl && styles.optionButtonSelected,
            ]}
            onPress={() => setSkillLevel(lvl)}
          >
            <Text
              style={[
                styles.optionButtonText,
                skillLevel === lvl && styles.optionButtonTextSelected,
              ]}
            >
              {lvl}
            </Text>
          </TouchableOpacity>
        ))}
      </View>
    </View>
  );

  if (!realmInstance && !playerToEditFromRoute) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.loadingContainer}>
          <Text>Carregando...</Text>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView
        contentContainerStyle={styles.scrollContainer}
        keyboardShouldPersistTaps="handled"
      >
        <View style={styles.formGroup}>
          <Text style={styles.label}>Nome do Jogador:</Text>
          <TextInput
            style={styles.input}
            value={name}
            onChangeText={setName}
            placeholder="Ex: Pelé"
            autoCapitalize="words"
          />
        </View>

        {renderPositionSelector()}
        {renderSkillSelector()}

        <TouchableOpacity style={styles.saveButton} onPress={handleSavePlayer}>
          <Text style={styles.saveButtonText}>
            {editingId ? "Salvar Alterações" : "Adicionar Jogador"}
          </Text>
        </TouchableOpacity>
      </ScrollView>
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
  scrollContainer: {
    padding: 20,
    paddingBottom: 40,
  },
  formGroup: {
    marginBottom: 20,
  },
  label: {
    fontSize: 16,
    color: "#333",
    marginBottom: 8,
    fontWeight: "500",
  },
  input: {
    backgroundColor: "#ffffff",
    borderWidth: 1,
    borderColor: "#ddd",
    borderRadius: 8,
    paddingHorizontal: 15,
    paddingVertical: 12,
    fontSize: 16,
    color: "#333",
  },
  selectorContainer: {
    marginBottom: 25,
  },
  optionsContainer: {
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "flex-start",
  },
  optionButton: {
    backgroundColor: "#e9ecef",
    paddingVertical: 10,
    paddingHorizontal: 15,
    borderRadius: 20,
    marginRight: 10,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: "#ced4da",
  },
  skillButton: {
    minWidth: 40,
    justifyContent: "center",
    alignItems: "center",
  },
  optionButtonSelected: {
    backgroundColor: "#6200ee",
    borderColor: "#6200ee",
  },
  optionButtonText: {
    fontSize: 14,
    color: "#212529",
  },
  optionButtonTextSelected: {
    color: "#ffffff",
    fontWeight: "bold",
  },
  saveButton: {
    backgroundColor: "#03dac6",
    paddingVertical: 15,
    borderRadius: 8,
    alignItems: "center",
    marginTop: 20,
    elevation: 2,
  },
  saveButtonText: {
    color: "#000",
    fontSize: 18,
    fontWeight: "bold",
  },
});

export default PlayerFormScreen;
