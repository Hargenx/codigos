import React from 'react';
import { View, FlatList, Image, Dimensions } from 'react-native';
import styles from '../style/estilo';

const GaleriaExemplo = ({ voltaPara }) => {
    const imagens = [
        'https://i.imgur.com/ohT0vQug.jpg',
        'https://i.imgur.com/5l0q2Wy.png',
        'https://i.blogs.es/c31a61/dragon-ball-daima-2024-octubre/375_375.webp',
        'https://www.einerd.com/wp-content/uploads/2021/10/red-ribbon-dragon-ball-e1634568621459-890x606.jpg',
        'https://i.imgur.com/pBewGong.jpghttps://i0.wp.com/i.imgur.com/MvfcBMV.png',
        'https://www.fayerwayer.com/resizer/v2/W6A3BTRSWBEYVDVFD4ZBO57RZE.jpg?auth=cacb1ba836bec9e81eac493d5540f52de91c2c71b7cac118c4ddcf8af0a9aa6f&width=1200&height=675&smart=true',
    ];

    return (
        <View style={styles.container}>
            <ScrollView contentContainerStyle={styles.container_sv}>
                {imagens.map((item, index) => (
                    <Image
                        key={index}
                        source={{ uri: item }}
                        style={styles.imagemGaleria}
                    />
                ))}
            </ScrollView>
            <Button title="Voltar" onPress={voltaPara} />
        </View>
    );
};

export default GaleriaExemplo;