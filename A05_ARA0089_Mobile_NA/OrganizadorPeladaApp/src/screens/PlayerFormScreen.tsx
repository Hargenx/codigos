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
import { Player } from "../types/player";
import { RootStackParamList } from "../navigation/AppNavigator";
// Para o Picker, você pode precisar de uma lib externa ou criar um customizado.
// Por simplicidade, usaremos TextInput, mas idealmente seria um Picker.
// Ex: import {Picker} from '@react-native-picker/picker';

type PlayerFormScreenNavigationProp = NativeStackNavigationProp<
  RootStackParamList,
  "PlayerForm"
>;
type PlayerFormScreenRouteProp = RouteProp<RootStackParamList, "PlayerForm">;

const POSITIONS: Player["position"][] = [
  "Goleiro",
  "Defensor",
  "Meio-campo",
  "Atacante",
  "Indefinido",
];
const SKILL_LEVELS: Player["skillLevel"][] = [1, 2, 3, 4, 5];

const PlayerFormScreen = () => {
  const navigation = useNavigation<PlayerFormScreenNavigationProp>();
  const route = useRoute<PlayerFormScreenRouteProp>();
  const playerToEdit = route.params?.playerToEdit;

  const [realmInstance, setRealmInstance] = useState<Realm | null>(null);
  const [name, setName] = useState(playerToEdit?.name || "");
  const [position, setPosition] = useState<Player["position"]>(
    playerToEdit?.position || "Indefinido"
  );
  const [skillLevel, setSkillLevel] = useState<Player["skillLevel"]>(
    playerToEdit?.skillLevel || 3
  );

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
  }, [navigation]);

  const handleSavePlayer = useCallback(async () => {
    if (!realmInstance) {
      Alert.alert("Erro", "Banco de dados não está pronto.");
      return;
    }
    if (name.trim() === "") {
      Alert.alert("Atenção", "O nome do jogador é obrigatório.");
      return;
    }

    try {
      realmInstance.write(() => {
        if (playerToEdit) {
          // Edição
          // Certifique-se que playerToEdit é um objeto Realm gerenciado
          // Se veio da navegação, pode ser um objeto JS puro. Precisamos buscar o objeto Realm.
          const playerInRealm = realmInstance.objectForPrimaryKey<Player>(
            "Player",
            playerToEdit._id
          );
          if (playerInRealm) {
            playerInRealm.name = name.trim();
            playerInRealm.position = position;
            playerInRealm.skillLevel = skillLevel;
          } else {
            Alert.alert("Erro", "Jogador não encontrado para edição.");
            return;
          }
        } else {
          // Criação
          realmInstance.create<Player>("Player", {
            _id: new BSON.ObjectId(),
            name: name.trim(),
            position,
            skillLevel,
            createdAt: new Date(),
          });
        }
      });
      navigation.goBack(); // Voltar para a lista
    } catch (error) {
      console.error("Falha ao salvar jogador:", error);
      Alert.alert("Erro", "Não foi possível salvar o jogador.");
    }
  }, [realmInstance, name, position, skillLevel, playerToEdit, navigation]);

  // Simples botões para simular um Picker
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
      <Text style={styles.label}>Nível de Habilidade:</Text>
      <View style={styles.optionsContainer}>
        {SKILL_LEVELS.map((lvl) => (
          <TouchableOpacity
            key={lvl}
            style={[
              styles.optionButton,
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

  if (!realmInstance && !playerToEdit) {
    // Se for edição, podemos mostrar o form mesmo sem realm ainda, pois os dados já existem
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
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.formGroup}>
          <Text style={styles.label}>Nome do Jogador:</Text>
          <TextInput
            style={styles.input}
            value={name}
            onChangeText={setName}
            placeholder="Ex: Neymar Jr."
          />
        </View>

        {renderPositionSelector()}
        {renderSkillSelector()}

        <TouchableOpacity style={styles.saveButton} onPress={handleSavePlayer}>
          <Text style={styles.saveButtonText}>
            {playerToEdit ? "Salvar Alterações" : "Adicionar Jogador"}
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
    marginBottom: 20,
  },
  optionsContainer: {
    flexDirection: "row",
    flexWrap: "wrap", // Permite que os botões quebrem linha
  },
  optionButton: {
    backgroundColor: "#e0e0e0",
    paddingVertical: 10,
    paddingHorizontal: 15,
    borderRadius: 20,
    marginRight: 10,
    marginBottom: 10,
  },
  optionButtonSelected: {
    backgroundColor: "#6200ee",
  },
  optionButtonText: {
    fontSize: 14,
    color: "#333",
  },
  optionButtonTextSelected: {
    color: "#fff",
    fontWeight: "bold",
  },
  saveButton: {
    backgroundColor: "#03dac6",
    paddingVertical: 15,
    borderRadius: 8,
    alignItems: "center",
    marginTop: 20,
  },
  saveButtonText: {
    color: "#000",
    fontSize: 18,
    fontWeight: "bold",
  },
});

export default PlayerFormScreen;
