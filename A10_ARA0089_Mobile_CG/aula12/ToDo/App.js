import { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, FlatList } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';


export default function App() {
  const [tarefa, definirTarefa] = useState('');
  const [tarefas, definirTarefas] = useState([]);
  useEffect(() => {
    // Carrega as tarefas salvas no AsyncStorage ao iniciar o aplicativo
    carregarTarefa();
  }, []);

  const carregarTarefa = async () => {
    try {
      const salvarTarefa = await AsyncStorage.getItem('tarefas');
      if (salvarTarefa !== null) {
        definirTarefas(JSON.parse(salvarTarefa));
      }
    } catch (error) {
      console.error('Erro ao carregar as tarefas:', error);
    }
  };
  const salvartarefa = async () => {
    try {
      const novaTarefa = [...tarefas, tarefa];
      await AsyncStorage.setItem('tarefas', JSON.stringify(novaTarefa));
      definirTarefas(novaTarefa);
      definirTarefa('');
    } catch (error) {
      console.error('Erro ao salvar a tarefa:', error);
    }
  };
    

  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 24, marginBottom: 10 }}>Lista de Tarefas</Text>
      <TextInput
        placeholder="Digite uma tarefa"
        value={tarefa}
        onChangeText={(text) => definirTarefa(text)}
        style={{ borderBottomWidth: 1, marginBottom: 10 }}
      />
      <Button title="Adicionar Tarefa" onPress={salvartarefa} />
      <FlatList
        data={tarefas}
        keyExtractor={(_, index) => index.toString()}
        renderItem={({ item }) => (
          <Text style={{ fontSize: 18, marginTop: 10 }}>{item}</Text>
        )}
      />
    </View>
  );
}

