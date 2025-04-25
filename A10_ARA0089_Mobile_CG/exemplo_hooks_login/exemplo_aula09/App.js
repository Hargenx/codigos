import React, { useState } from 'react';
import { View } from 'react-native';
import LoginScreen from './screens/LoginScreen';
import CadastroScreen from './screens/CadastroScreen';
import HomeScreen from './screens/HomeScreen';
import { styles } from './styles/styles';

const App = () => {
  const [telaAtual, setTelaAtual] = useState('login'); // 'login', 'cadastro', ou 'home'
  const [usuarioCadastrado, setUsuarioCadastrado] = useState('');
  const [senhaCadastrada, setSenhaCadastrada] = useState('');

  const [usuarioLogado, setUsuarioLogado] = useState('');

  return (
    <View style={styles.container}>
      {telaAtual === 'login' && (
        <LoginScreen
          mudarTela={setTelaAtual}
          usuarioCadastrado={usuarioCadastrado}
          senhaCadastrada={senhaCadastrada}
          setUsuarioLogado={setUsuarioLogado}
        />
      )}
      {telaAtual === 'cadastro' && (
        <CadastroScreen
          mudarTela={setTelaAtual}
          setUsuarioCadastrado={setUsuarioCadastrado}
          setSenhaCadastrada={setSenhaCadastrada}
        />
      )}
      {telaAtual === 'home' && (
        <HomeScreen
          usuarioLogado={usuarioLogado}
          mudarTela={setTelaAtual}
        />
      )}
    </View>
  );
};

export default App;
