import React from 'react';
import { Controller, useForm } from 'react-hook-form';
import * as Yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';
import styled from 'styled-components/native';
import { Game } from '../types/Game';

interface GameFormProps {
  onSubmit: (data: Game) => void;
  defaultValues?: Game;
}

const schema = Yup.object().shape({
  title: Yup.string().required('Título é obrigatório'),
  genre: Yup.string().required('Gênero é obrigatório'),
  releaseYear: Yup.number()
    .typeError('Ano deve ser numérico')
    .required('Ano é obrigatório'),
});

export function GameForm({ onSubmit, defaultValues }: GameFormProps): JSX.Element {
  const { control, handleSubmit, formState: { errors } } = useForm<Game>({
    resolver: yupResolver(schema),
    defaultValues: defaultValues || { title: '', genre: '', releaseYear: new Date().getFullYear() },
  });

  return (
    <FormContainer>
      <Label>Título</Label>
      <Controller
        control={control}
        name="title"
        render={({ field: { onChange, value } }) => (
          <Input value={value} onChangeText={onChange} placeholder="Nome do jogo" />
        )}
      />
      {errors.title && <ErrorText>{errors.title.message}</ErrorText>}

      <Label>Gênero</Label>
      <Controller
        control={control}
        name="genre"
        render={({ field: { onChange, value } }) => (
          <Input value={value} onChangeText={onChange} placeholder="Gênero" />
        )}
      />
      {errors.genre && <ErrorText>{errors.genre.message}</ErrorText>}

      <Label>Ano de Lançamento</Label>
      <Controller
        control={control}
        name="releaseYear"
        render={({ field: { onChange, value } }) => (
          <Input
            value={String(value)}
            onChangeText={(text) => onChange(Number(text))}
            placeholder="2023"
            keyboardType="numeric"
          />
        )}
      />
      {errors.releaseYear && <ErrorText>{errors.releaseYear.message}</ErrorText>}

      <SubmitButton onPress={handleSubmit(onSubmit)}>
        <ButtonText>Salvar</ButtonText>
      </SubmitButton>
    </FormContainer>
  );
}

const FormContainer = styled.ScrollView`
  flex: 1;
  padding: 16px;
`;
const Label = styled.Text`
  font-weight: bold;
  margin-top: 12px;
`;
const Input = styled.TextInput`
  border: 1px solid #ccc;
  padding: 8px;
  border-radius: 4px;
  margin-top: 4px;
`;
const ErrorText = styled.Text`
  color: red;
  margin-top: 4px;
`;
const SubmitButton = styled.TouchableOpacity`
  background-color: #4caf50;
  padding: 12px;
  border-radius: 4px;
  align-items: center;
  margin-top: 24px;
`;
const ButtonText = styled.Text`
  color: #fff;
  font-weight: bold;
`;