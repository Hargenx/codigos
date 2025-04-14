import {  Dimensions } from 'react-native';

const larguraTela = Dimensions.get('window').width;
const tamanhoImagem = larguraTela / 3 - 10;
import { StyleSheet } from 'react-native'; const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'lightblue',
        padding: 10,
        marginTop: 40,
    },
    container_sv: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        justifyContent: 'space-between',
    },
    item: {
        fontSize: 18,
        marginVertical: 5,
        textAlign: 'center',
    },
    sectionHeader: {
        fontSize: 24,
        backgroundColor: 'lightgray',
        padding: 10,
    },
    carouselContainer: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    carouselItem: {
        fontSize: 24,
    },
    page: {
        width: 400,
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    text: {
        fontSize: 24,
        fontWeight: 'bold',
        color: 'white',
    },
    pageIndicator: {
        textAlign: 'center',
        fontSize: 18,
        marginTop: 10,
    },
    buttonSpacing: {
        marginTop: 10,
    },
    button: {
        marginBottom: 10,
        width: '100%',
        height: 50,
        flexDirection: 'row',
        padding: 10,
        justifyContent: 'space-between',
    },
    imagemGaleria: {
        width: tamanhoImagem,
        height: tamanhoImagem,
        marginBottom: 10,
        borderRadius: 8,
    },
});
export default styles;
