# 🚦 Semáforo com ESP32 usando MicroPython (IoT - SENAI)
![Tela Principal](.wokwi.png)

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de **Internet das Coisas (IoT)** no curso de **Desenvolvimento de Sistemas** do **SENAI**.

O desafio consistia em simular um sistema de **semáforo com 3 LEDs (Verde, Amarelo e Vermelho)** utilizando a plataforma Wokwi e a placa **ESP32**.

## ✅ O que foi proposto

Criar um circuito e um programa que controle três LEDs representando as cores do semáforo com as seguintes regras de temporização:

- **Verde:** 20 segundos  
- **Amarelo:** 10 segundos  
- **Vermelho:** 7 segundos  
- Intervalo de **0.5 segundos** entre os estados

O comportamento deve ser contínuo, dentro de um **laço infinito**, simulando o funcionamento de um semáforo real.

## 🔧 Tecnologias e Ferramentas

- Microcontrolador: **ESP32**
- Plataforma de simulação: **Wokwi**
- Linguagem: **MicroPython**

---

## 🎯 O que foi feito

- Foi montado um circuito no Wokwi com 3 LEDs e resistores conectados ao ESP32.
- Desenvolvido um código em MicroPython que liga e desliga os LEDs com os tempos corretos.
- Foram utilizados comandos de controle de pinos (`Pin`) e temporização (`sleep`).
- As mensagens correspondentes a cada cor foram impressas no console, facilitando o entendimento da lógica.

---

## Autores
- Giovanna Xavier - Desenvolvedora e estudante de Desenvolvimento de Sistemas no [Senai Jandira](https://sp.senai.br/unidade/jandira/). Conecte-se no [LinkedIn](https://www.linkedin.com/in/giovanna-xavier-978538241/).
