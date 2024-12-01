import streamlit as st # type: ignore
from views import View
from datetime import datetime
import time

class AbrirAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Agenda do Dia")
        AbrirAgendaUI.abrir_agenda()
    @staticmethod
    def abrir_agenda():
        data = st.date_input("Informe a data")
        hinicio = st.time_input("Informe o horário inicial")
        hfim = st.time_input("Informe o horário final")
        intervalo = st.time_input("Informe o intervalo entre os horários (minutos)")
        if st.button("Inserir Horários"):
            View.horario_abrir_agenda(data, hinicio, hfim, intervalo)
            st.success("Horário(s) inserido(s) com sucesso")
            time.sleep(2)
            st.rerun()
