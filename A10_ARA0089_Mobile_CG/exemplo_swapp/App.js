import React, { useState } from 'react';
import { View, Button } from 'react-native';
import FlatListExemplo from './exemplos/FlatListExemplo';
import SectionListExemplo from './exemplos/SectionListExemplo';
import ScrollViewExemplo from './exemplos/ScrollViewExemplo';
import CarouselExemplo from './exemplos/CarouselExemplo';
import outro_exemplo from './exemplos/outro';
import styles from './style/estilo';


export default function App() {
  const [telaAtual, setTelaAtual] = useState(null);
  const navepaParaTela = (nomeTela) => {
    setTelaAtual(nomeTela);
  };
  const desenhaTela = () => {
    switch (telaAtual) {
      case 'FlatList':
        return <FlatListExemplo voltaPara={() => setTelaAtual(null)} />;
      case 'SectionList':
        return <SectionListExemplo voltaPara={() => setTelaAtual(null)} />;
      case 'ScrollView':
        return <ScrollViewExemplo voltaPara={() => setTelaAtual(null)} />;
      case 'Carousel':
        return <CarouselExemplo voltaPara={() => setTelaAtual(null)} />;
      case 'Outro':
        return <outro_exemplo voltaPara={() => setTelaAtual(null)} />;
      default:

        return (
          <View style={styles.container}>
            <Button title="FlatList Exemplo" onPress={() => navepaParaTela('FlatList')} />
            <View style={styles.buttonSpacing} />
            <Button title="SectionList Exemplo" onPress={() => navepaParaTela('SectionList')} />
            <View style={styles.buttonSpacing} />
            <Button title="ScrollView Exemplo" onPress={() => navepaParaTela('ScrollView')} />
            <View style={styles.buttonSpacing} />
            <Button title="Carousel Exemplo" onPress={() => navepaParaTela('Carousel')} />
            <View style={styles.buttonSpacing} />
            <Button title="Outro Exemplo" onPress={() => navepaParaTela('Outro')} />
          </View>
        );
    }
  };
  return (
    <View style={styles.container}>
      {desenhaTela()}
    </View>
  );
}
