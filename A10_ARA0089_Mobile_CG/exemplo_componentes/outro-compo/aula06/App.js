import React, { useState } from 'react';
import { View, Text, FlatList, TouchableOpacity, Modal, TextInput, Button as RNButton, Switch } from 'react-native';

const App = () => {
  const [tasks, setTasks] = useState([
    { id: '1', text: 'Estudar JSX', completed: false },
    { id: '2', text: 'Estudar React', completed: true },
    { id: '3', text: 'Terminar projeto', completed: false },
  ]);

  const [isModalVisible, setModalVisible] = useState(false);
  const [newTaskText, setNewTaskText] = useState('');

  const toggleTaskStatus = (taskId) => {
    setTasks((prevTasks) =>
      prevTasks.map((task) =>
        task.id === taskId ? { ...task, completed: !task.completed } : task
      )
    );
  };

  const addNewTask = () => {
    if (newTaskText.trim() !== '') {
      setTasks((prevTasks) => [
        ...prevTasks,
        { id: (prevTasks.length + 1).toString(), text: newTaskText, completed: false },
      ]);
    }
    setModalVisible(false);
    setNewTaskText('');
  };


  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 20, marginBottom: 20, marginTop: 20 }}>Lista de Tarefas</Text>
      <FlatList
        data={tasks}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View
            style={{
              flexDirection: 'row',
              justifyContent: 'space-between',
              alignItems: 'center',
              marginBottom: 10,
            }}
          >
            <View style={{ flex: 1 }}>
              <Text style={{ fontSize: 16 }}>{item.text}</Text>
            </View>
            <View style={{ flexDirection: 'row', alignItems: 'center' }}>
              <Switch
                value={item.completed}
                onValueChange={() => toggleTaskStatus(item.id)}
              />
              <Text style={{ color: item.completed ? 'green' : 'red' }}>
                {item.completed ? 'Concluída' : 'Pendente'}
              </Text>
            </View>
          </View>
        )}
      />

      <TouchableOpacity
        onPress={() => setModalVisible(true)}
        style={{
          backgroundColor: 'blue',
          padding: 12,
          borderRadius: 5,
          alignItems: 'center',
        }}
      >
        <Text style={{ color: 'white', fontSize: 16 }}>Adicionar Tarefa</Text>
      </TouchableOpacity>
      <Modal visible={isModalVisible} animationType="slide">
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
          <Text style={{ fontSize: 20, marginBottom: 20 }}>Nova Tarefa</Text>
          <TextInput
            placeholder="Digite a nova tarefa"
            style={{
              borderColor: 'gray',
              borderWidth: 1,
              padding: 10,
              width: '80%',
              marginBottom: 10,
            }}
            onChangeText={(text) => setNewTaskText(text)}
            value={newTaskText}
          />
          <View style={{ flexDirection: 'row' }}>
            <RNButton
              title="Adicionar"
              onPress={addNewTask}
              color="blue"
              style={{ flex: 1 }}
            />
            <RNButton
              title="Cancelar"
              onPress={() => setModalVisible(false)}
              color="orange"
              style={{ flex: 1 }}
            />
          </View>
        </View>
      </Modal>
    </View>
  );
};

export default App;
