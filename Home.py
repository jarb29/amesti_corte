import streamlit as st
import pandas as pd
import numpy as np
import boto3
import json
import datetime
import plotly.express as px
import datetime
from io import StringIO
import matplotlib.pyplot as plt

st.title(":bar_chart: Corte Dashboard.")
st.markdown("##")


@st.cache_data
def total(df):
    columns_names  = ['Tiempo del mensaje Máquina', 'Puesto de trabajo', 'Programa principal',
       'Estado', 'Denominación del pedido de producción', 'Número Real',
       'Chapa actual', 'Nº lote', 'Bruto Tiempo de ejecución del programa',
       'Neto Tiempo de ejecución del programa', 'Neto Tiempo mecaniz.',
       'Lugar de emplazamiento', 'Centro de costes', 'Agrupación']
    columns_drop = ['Estado', 'Denominación del pedido de producción', 'Número Real',
       'Chapa actual', 'Nº lote', 'Lugar de emplazamiento', 'Centro de costes', 'Agrupación']
    
    df = df.drop(columns_drop, axis=1) 
    df = df.rename(columns={'Tiempo del mensaje Máquina': "Tiempo", 
                            'Puesto de trabajo': "Laser",
                            'Programa principal': "Programa",
                            'Bruto Tiempo de ejecución del programa': "Tiempo_Bruto",
                            'Neto Tiempo de ejecución del programa': "Tiempo_Neto",
                            'Neto Tiempo mecaniz.': "Tiempo_Mecanizado",})
    
    return df




uploaded_file = st.file_uploader("Cargue el archivo")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df = total(df)
    st.write(df)
    



# # ---- SIDEBAR ----
# st.sidebar.header("Please Filter Here:")



# sortedDates = sorted([datetime.datetime.strptime(item, '%Y-%m-%d') for item in df["date"].unique()])
# sortedDates = [item.strftime('%Y-%m-%d') for item in sortedDates]


    laser = st.sidebar.multiselect(
        "Select Laser:",
        options=df['Laser'].unique(),
        default=df['Laser'].unique()
    )

    programa = st.sidebar.multiselect(
        "Select programa:",
        options=df['Programa'].unique(),
        default=df['Programa'].unique()[0:10],
    )



    df_selection = df.query(
        "Laser == @laser & Programa == @programa "
    )

# # ---- MAINPAGE ----


# # TOP KPI's\
    total_tiempo = round(df["Tiempo_Bruto"].sum()/60, 2)
    date_tiempo = round(df_selection["Tiempo_Bruto"].sum()/60, 2)
    programas = round(df['Programa'].nunique(), 1)
    programas_selected = round(df_selection['Programa'].nunique(), 1)
    # date_average_earning = round(df_selection['Programas'].nunique(), 1)
    # date_average_loosing = round(df_selection['profit'][df['profit_'] == 1].mean(), 1)
    # length_average_earning = len(df['profit'][df['profit_'] == 0])
    # length_average_loosing = len(df['profit'][df['profit_'] == 1])
    # date_length_average_earning = len(df_selection['profit'][df['profit_'] == 0])
    # date_length_average_loosing = len(df_selection['profit'][df['profit_'] == 1])
    # total_symbol = len(df['symbol'].unique())
    # date_symbol = len(df_selection['symbol'].unique())

    left_column, middle_column = st.columns(2)
    with left_column:
        # st.text('___'*10)
        # st.subheader("Total Earning:")
        # st.subheader(f"US $ {total_sales:,}")
        st.text('___'*10)
        st.subheader("Total Horas trabajadas:")
        st.subheader(f"{total_tiempo}")
        st.text('___'*10)
        st.subheader("Total Programas cortados:")
        st.subheader(f"Total: {programas}")

        # st.text('___'*10)
        # st.subheader("Total Wrong choices:")
        # st.subheader(f"Total: {length_average_loosing}")
        # st.text('___'*10)
        # st.subheader("Total Average Loosing:")
        # st.subheader(f"US $ {average_loosing }")
        # st.text('___'*10)
        # st.subheader("Total Symbols Trade:")
        # st.subheader(f"Total: {total_symbol}")
    
    



    with middle_column:
        # st.text('___'*10)
        # st.subheader("Date Earning:")
        # st.subheader(f"US $ {date_sales:,}")
        st.text('___'*10)
        st.subheader("Horas programas seleccionados")
        st.subheader(f"{date_tiempo}")
        st.text('___'*10)
        st.subheader("# Programas seleccionados:")
        st.subheader(f"Total: {programas_selected}")

        # st.text('___'*10)
        # st.subheader("# Date Wrong choices:")
        # st.subheader(f"Total: {date_length_average_loosing}")
        # st.text('___'*10)
        # st.subheader("Date Average Loosing:")
        # st.subheader(f"US $ {date_average_loosing }")
        # st.text('___'*10)
        # st.subheader("Date Symbols Trade:")
        # st.subheader(f"Total: {date_symbol}")

# st.markdown("""---""")


# # SALES BY PRODUCT LINE [BAR CHART]
    sales_by_product_line = (
        df_selection.groupby('Programa') \
       .agg(count=('Programa', 'size'), tiempo_promedio=('Tiempo_Bruto', 'mean')) \
       .reset_index()
       
    )
    fig_product_sales = px.bar(
        sales_by_product_line,
        x="Programa",
        y='tiempo_promedio',
        # orientation="h",
        title="<b>Promedios</b>",
        color_discrete_sequence=["#0063B8"] * len(sales_by_product_line),
        template="plotly_dark",
    )
    fig_product_sales.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )

# # SALES BY HOUR [BAR CHART]
# sales_by_hour = df_selection.groupby(by=["symbol"]).sum()[["profit"]]
# fig_hourly_sales = px.bar(
#     sales_by_hour,
#     y=sales_by_hour.index,
#     x="profit",
#     orientation="h",
#     title="<b>Profit by Symbol</b>",
#     color_discrete_sequence=["#CC6600"] * len(sales_by_hour),
#     template="plotly_dark",
# )
# fig_hourly_sales.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
# )
    st.plotly_chart(fig_product_sales, use_container_width=True)
    st.markdown("""---""")
# st.plotly_chart(fig_hourly_sales, use_container_width=True)
# st.markdown("""---""")




# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# # To run the model
# # source .venv/bin/activate
# # streamlit run Home.py


# # Funcion para obtener el ultimo numero en la celda (espsor)
# def last_number(x):
#     number = [5, 8, 1, 2, 3, 4, 6]
#     reverse = reverse_string(x)
#     letter = [char for char in reverse]
#     number = numeric(letter)
#     number = not_none(number)

#     return number

# # Funcion para revertir el string
# def reverse_string(x):  
#     str1 = ""   # Declaring empty string to store the reversed string  
#     for i in x:  
#         str1 = i + str1  
#     return str1    # It will return the reverse string to the caller function  

# # Funcio para verificar el numero
# def numeric(x):
#     for each in x:
#         if each.isdigit():
#             if each == '0':
#                 return 3
#             if each == '8':
#                 return 0.8
#             if each == '9':
#                 return 4
#             if each == '5':
#                 return 0.5
#             else:
#                 return int(each)
# def not_none(x):
#     if x == None:
#         return 4
#     else:
#         return x
    
# def tobera5030(x):
#     if x>3:
#         return 70
#     elif x>2 and x<=3:
#         return 41
#     elif x>=1 and x<=2:
#         return 36
#     else:
#         return 16
    
# # Funcion para agregar el area de la plancha
# def area_plancha(x):
#     reverse = reverse_string(x)
    
#     letter = list(reverse)
    
#     if letter[2] == 'A':
#                 return 3*1
#     if letter[2] == 'B':
#                 return 2.5*1    
#     if letter[2] == 'C':
#                 return 2*1
#     if letter[2] == 'D':
#                 return 1.5*3
#     if letter[2] == 'E':
#                 return 1.5*2.5
#     if letter[2] == 'F':
#                 return 1.5*2            
#     if letter[2] == 'G':
#                 return 1*3
#     if letter[2] == 'H':
#                 return 1*1.1



            
# # Funcio para obtener el tiempo cortado por espesor en los laser 5030
# def tiempo_espesor_L5030(x):
#     df_hist = x.drop(['Lugar de emplazamiento', 'Centro de costes', 'Agrupación', 'Nº lote', 'Estado', 'Número Real', 'Denominación del pedido de producción'], axis=1)
#     df_hist['Dia'] = df_hist['Tiempo del mensaje Máquina'].dt.date
#     df_hist['Hora'] = df_hist['Tiempo del mensaje Máquina'].dt.time
#     df_hist_L5030 = df_hist[(df_hist['Puesto de trabajo'] == 'Laser#1') | (df_hist['Puesto de trabajo'] == 'Laser#2')]
#     grouped_his_L5030 = df_hist_L5030.groupby('Programa principal') \
#        .agg(count=('Programa principal', 'size'), tiempo_promedio=('Bruto Tiempo de ejecución del programa', 'mean')) \
#        .reset_index()
#     grouped_his_L5030['espesor'] = grouped_his_L5030['Programa principal'].apply(last_number)
#     grouped_his_L5030['tiempo horas'] = round(grouped_his_L5030['count'] * grouped_his_L5030['tiempo_promedio']/60, 2)
#     grouped_his_L5030 = grouped_his_L5030.drop(['Programa principal', 'count', 'tiempo_promedio'], axis=1)
#     grouped_total = grouped_his_L5030.copy()
#     new_grouped = grouped_total.groupby('espesor') \
#        .agg(tiempo_horas=('tiempo horas', 'sum'))\
#        .reset_index()
#     new_grouped['tobera m3/hr'] = new_grouped["espesor"].apply(tobera5030)
#     new_grouped['nitrox m3'] = round(new_grouped['tobera m3/hr'] * new_grouped['tiempo_horas'] )
#     new_grouped['nitrox kg'] = round(new_grouped['nitrox m3'] * 0.84 )
# #     new_grouped['area'] = grouped_his_L5030['Programa principal'].apply(area_plancha)
#     return new_grouped

# # Funcio para obtener el tiempo cortado por espesor en los laser 3030
# def tiempo_espesor_L3030(x):
#     df_hist = x.drop(['Lugar de emplazamiento', 'Centro de costes', 'Agrupación', 'Nº lote', 'Estado', 'Número Real', 'Denominación del pedido de producción'], axis=1)
#     df_hist['Dia'] = df_hist['Tiempo del mensaje Máquina'].dt.date
#     df_hist['Hora'] = df_hist['Tiempo del mensaje Máquina'].dt.time
#     df_hist_L5030 = df_hist[(df_hist['Puesto de trabajo'] == 'Laser#3')]
#     grouped_his_L5030 = df_hist_L5030.groupby('Programa principal') \
#        .agg(count=('Programa principal', 'size'), tiempo_promedio=('Bruto Tiempo de ejecución del programa', 'mean')) \
#        .reset_index()
#     grouped_his_L5030['espesor'] = grouped_his_L5030['Programa principal'].apply(last_number)
#     grouped_his_L5030['tiempo horas'] = round(grouped_his_L5030['count'] * grouped_his_L5030['tiempo_promedio']/60, 2)
#     grouped_his_L5030 = grouped_his_L5030.drop(['Programa principal', 'count', 'tiempo_promedio'], axis=1)
#     grouped_total = grouped_his_L5030.copy()
#     new_grouped = grouped_total.groupby('espesor') \
#        .agg(tiempo_horas=('tiempo horas', 'sum'))\
#        .reset_index()
#     new_grouped['tobera m3/hr'] = new_grouped["espesor"].apply(lambda x: 27 if x < 2 else 61)
#     new_grouped['nitrox m3'] = round(new_grouped['tobera m3/hr'] * new_grouped['tiempo_horas'] )
#     new_grouped['nitrox kg'] = round(new_grouped['nitrox m3'] / 0.84 )
# #     new_grouped['area'] = grouped_his_L5030['Programa principal'].apply(area_plancha)
#     return new_grouped



modelos_nuevos = {
    '05RB050001ABC':{
        'modelo' : 'RB',
        'cantidad':14
    },
    '05N0450002BBC':{
        'modelo' : 'N450',
        'cantidad':8
    },
    '05RB050002AAC':{
        'modelo' : 'RB',
        'cantidad':1
    },
    '05N03500_8AAZ':{
        'modelo' : 'N350',
        'cantidad':24,
        "tpn":3
    },
    '05N0450002BAC':{
        'modelo' : 'N450',
        'cantidad':1
    },
    '05SC380002CAC':{
        'modelo' : 'SC380',
        'cantidad':1,
        "tpn":3
    },
    '05C400B002ACC':{
        'modelo' : 'C400',
        'cantidad':5
    },
    '05N0380002CAC':{
        'modelo' : 'N380',
        'cantidad':1
    },

    '05N03800_8AAZ':{
        'modelo' : 'N380',
        'cantidad':14
    },

    '05RB050005AAC':{
        'modelo' : 'RB',
        'cantidad':4
    },
    '05CALLR0_8ACZ':{
        'modelo' : 'COCINA',
        'cantidad':14,
        "tpn":4
    },
    '05R450D0_8AAZ':{
        'modelo' : 'R450D',
        'cantidad':11
    },
    '05N0350002AAC':{
        'modelo' : 'N350',
        'cantidad':2,
        "tpn":5
    },
    '05R450D002ABC':{
        'modelo' : 'R450D',
        'cantidad':2,
        "tpn":4
    },
    '05Y81CH0_8ACZ':{
        'modelo' : 'I8100+',
        'cantidad':2,
        "tpn":5
    },
    '05CALLR002AAC':{
        'modelo' : 'COCINA',
        'cantidad':2,
        "tpn":6
    },
    '05Y700R001AAC':{
    },
    '05C400B002AAC':{
        'modelo' : 'C400',
        'cantidad':2,
        'tpn':4
    },
    '05C400B008AAZ':{
        'modelo' : 'C400',
        'cantidad':10
    },
    '05Y81CH0_8ABZ':{
        'modelo' : 'I8100+',
        'cantidad':2,
        "tpn":7
    },
    '05C400B002ABC':{
        'modelo' : 'C400',
        'cantidad':6,

    },
    '05N0450003AAC':{
        'modelo' : 'N450',
        'cantidad':10
    },
    '05Y81CH002AAC':{
        'modelo' : 'I8100+',
        'cantidad':1,
        "tpn":7
    },
    '05R450D002AAC':{
        'modelo' : 'R450D',
        'cantidad':8,
        "tpn":8
    },
    '05R450D003ABC':{
        'modelo' : 'R450D',
        'cantidad':4,
        "tpn":7
    },
    '05N0380003AAC':{
        'modelo' : 'N380',
        'cantidad':10
    },
    '05RB050004AAC':{
        'modelo' : 'RB',
        'cantidad':5
    },
    '05R450D003AAC':{
        'modelo' : 'R450D',
        'cantidad':6,
        "tpn":10
    },
    '05RB050003AAC':{
        'modelo' : 'RB',
        'cantidad':10
    },
    '05RB050004ABC':{
        'modelo' : 'RB',
        'cantidad':5
    },
    '05N0350003AAC':{
        'modelo' : 'N350',
        'cantidad':14,
        "tpn":12
    },
    '05Y81CH0_8AAZ':{
        'modelo' : 'I8100+',
        'cantidad':4,
        "tpn":11
    },
    '05N0450004AAC':{
        'modelo' : 'N450',
        'cantidad':2
    },
    '05N0380004AAC':{
        'modelo' : 'N380',
        'cantidad':2
    },
    '05N0350004AAC':{
        'modelo' : 'N350',
        'cantidad':4,
        "tpn":23
    },
    '05N0380004ABC':{
        'modelo' : 'N380',
        'cantidad':10
    },
    '05C400B003ABC':{
        'modelo' : 'C400',
        'cantidad':21
    },
    '05CALVI1_5AAI':{
        'modelo' : 'COCINA',
        'cantidad':4,
        "tpn":10
    },
    '05C400B003AAC':{
        'modelo' : 'C400',
        'cantidad':3
    },
    '05N0450004ABC':{
        'modelo' : 'N450',
        'cantidad':8
    },
    '05R450D004AAC':{
        'modelo' : 'R450D',
        'cantidad':4,
        "tpn":21
    },
    '05C400B004AAC':{
        'modelo' : 'C400',
        'cantidad':2,
        'tpn':17
    },
    '05SC380004AAC':{
        'modelo' : 'SC380',
        'cantidad':2,
        "tpn":17
    },
    '05Y81CH004AAC':{
        'modelo' : 'I8100+',
        'cantidad':6,
        "tpn":16
    },
    '05RB050005ABC':{
        'modelo' : 'RB',
        'cantidad':4
    },
    '05N0450004ACC':{
        'modelo' : 'N450',
        'cantidad':16
    },
    '05CALLR006AAC':{
        'modelo' : 'COCINA',
        'cantidad':6,
        "tpn":24
    },
    '05Y81CH003AAI': {
        'modelo' : 'I8100+',
        'cantidad':42,
        "tpn":66
    },

    ##############
    "ESP_DEFLECT0R_3MM":{
        'modelo' : 'N350',
        'cantidad':15,
        "tpn":7
    },
        "C5003_CENI_08":{
        'modelo' : 'C500',
        'cantidad':13,
        "tpn":3
    },
        "REJILLA_3MM_2000":{
        'modelo' : 'FLEJES',
        'cantidad':9,
        "tpn":21
    },
        "CAIN0X2_C0NJI_1":{
        'modelo' : 'COCINA',
        'cantidad':1,
        "tpn":4
    },
        "C500_3_C0NJ_08MM":{
        'modelo' : 'C500',
        'cantidad':2.5,
        "tpn":2
    },
        "05CALVI0_5IAI":{
        'modelo' : 'COCINA',
        'cantidad':5,
        "tpn":2
    },
        "05SC380002AAC_BM":{
        'modelo' : 'SC380',
        'cantidad':1,
        "tpn":3
    },
        "05S380T003BAC":{
        'modelo' : 'SC380',
        'cantidad':39,
        "tpn":12
    },
        "05I800P002ABC":{
        'modelo' : 'INSERTO3',
        'cantidad':3,
        "tpn":5
    },
        "05CALVI1_5ABI":{
        'modelo' : 'COCINA',
        'cantidad':22,
        "tpn":10
    },
        "05S380T003AAC":{
        'modelo' : 'SC380',
        'cantidad':11,
        "tpn":5
    },
        "05I800P006AAC":{
        'modelo' : 'INSERTO3',
        'cantidad':12,
        "tpn":26
    },

# Corresponde  a modelos que se cortaron pero con la nomenclatura vieja

      'ESP_CENICER0_II':{
        'modelo' : 'COCINA',
        'cantidad':2
    },
      'ESP_0BSTRUCTIR_IN':{
        'modelo' : 'COCINA',
        'cantidad':2
    },
      'ESP_PR0T_SENIC':{
        'modelo' : 'COCINA',
        'cantidad':2
    },
      'N350_3_4MM_I':{
        'modelo' : 'N350',
        'cantidad':2
    },
      'ESP_TECH0_F0ND_L':{
        'modelo' : 'COCINA',
        'cantidad':2
    },
      'ESP_2MM_LE_450':{
        'modelo' : 'COCINA',
        'cantidad':2
    },
      '1_5MM_IN0X':{
        'modelo' : 'COCINA',
        'cantidad':2
    },
      'ESP_CUB_BASE_CEN':{
        'modelo' : 'COCINA',
        'cantidad':2
    },
      'ESP_PR0TEC_INF':{
        'modelo' : 'COCINA',
        'cantidad':2
    },
      'BASE_900_2MM':{
        'modelo' : 'BASES',
        'cantidad':3
    },
      'CAIN0X2_C0NJII_1':{
        'modelo' : 'COCINA',
        'cantidad':14
    },
      'C0D0S6P_05MM':{
        'modelo' : 'CODOS_HOJALATA',
        'cantidad':6
    },
      'CAIN0X2_C0NJ_4MM':{
        'modelo' : 'COCINA',
        'cantidad':12,
        "tpn":24
    },
      'CAIN0X2_F0ND0_05':{
        'modelo' : 'COCINA',
        'cantidad':5
    },
      'CAIN0X2_C0NJII_3':{
        'modelo' : 'COCINA',
        'cantidad':8,
        "tpn":14
    },
      'CAIN0X2_C0NJII_08':{
        'modelo' : 'COCINA',
        'cantidad':5,
        "tpn":3
    },
      'CAIN0X2_C0NJI_08':{
        'modelo' : 'COCINA',
        'cantidad':5,
        "tpn":3
    },
      'CAIN0X2_C0NJI_3MM':{
        'modelo' : 'COCINA',
        'cantidad':2,
        "tpn":13
    },
      'CAIN0X2_PAN_LAT':{
        'modelo' : 'COCINA',
        'cantidad':2,
        "tpn":3
    },
      'CAIN0X2_C0NJ_05MM':{
        'modelo' : 'COCINA',
        'cantidad':1,
        "tpn":3
    },
    'I8100P_1_PAN_C400':{
        'modelo' : 'I8100+',
        'cantidad':2,
        "tpn":5

    },
    '05C500B002AAC':{
        'modelo' : 'C500',
        'cantidad':3,
        'tpn':3
    },
    '05C500B002ABC':{
        'modelo' : 'C500',
        'cantidad':2,
        'tpn':6
    },
    '05C500B003AAC':{
        'modelo' : 'C500',
        'cantidad':5,
        'tpn':9
    },
    '05C500B004AAC':{
        'modelo' : 'C500',
        'cantidad':2,
        'tpn':17
    },

# Corresponde a los modelos que tienen el nuevo nombre pero no se pudieron analizar

    '05RB050001AAC':{
        'modelo' : 'RB',
        'cantidad':14
    },
    '05SC3800_8AAZ':{
        'modelo' : 'SC380',
         'cantidad':12,
         "tpn":2
    },
    '05N0380002AAC':{
        'modelo' : 'N380',
        'cantidad':1
    },
    '05N04500_8AAZ':{
        'modelo' : 'N450',
        'cantidad':14
    },
    '05C400B0_8ABZ':{
        'modelo' : 'C400',
        'cantidad':3
    },
    '05CALVI1':{
        'modelo' : 'COCINA',
        'cantidad':12
    },
    '05I800P004ABC': {
        'modelo' : 'INSERTO3',
        'cantidad':3
    },
    '05I800P002AAC': {
        'modelo' : 'INSERTO3',
        'cantidad':2,
        "tpn":11
    },
    '05CALVI4AAI': {
        'modelo' : 'COCINA',
        'cantidad':22,
        "tpn":14
    },
    '05I800P004AAC': {
        'modelo' : 'INSERTO3',
        'cantidad':2
    },
    '05N0350004ABC': {
        'modelo' : 'N350',
        'cantidad':6,
        "tpn":18
    },
    '05I800P003AAC': {
        'modelo' : 'INSERTO3',
        'cantidad':8,
        "tpn":11
    },
    '05SC380002AAC_B': {
        'modelo' : 'SC380',
        'cantidad':1,
        "tpn":3
    },
    "CAIN0X2_C0NJ_6MM": {
        'modelo' : 'COCINA',
        'cantidad':6,
        "tpn":24
    },
    "05I800P001AAC": {
        'modelo' : 'INSERTO3',
        'cantidad':36,
        "tpn":15
    },
    "RACK_L1200_4MM": {
        'modelo' : 'Planta',
        'cantidad':4,
        "tpn":9
    },
    "05CALVI1AAC": {
        'modelo' : 'COCINA',
        'cantidad':2,
        "tpn":3
    },
    "05N0360003AAC": {
        'modelo' : 'N3604',
        'cantidad':11,
        "tpn":12
    },
    "05N0360002AAC": {
        'modelo' : 'N3604',
        'cantidad':2,
        "tpn":4
    },
    "05N0360004AAC": {
        'modelo' : 'N3604',
        'cantidad':2,
        "tpn":18
    },
    "05N03600_8AAZ": {
        'modelo' : 'N3604',
        'cantidad':24,
        "tpn":3
    },
     "05RB0500_8AAC": {
        'modelo' : 'RB',
        'cantidad':21,
        "tpn":2
    },
     "05RB0500_8ABC": {
        'modelo' : 'RB',
        'cantidad':14,
        "tpn":1
    },

    "ESP_T0LVA_P0ST_II": {
        'modelo' : 'I8100+',
        'cantidad':5,
        "tpn":10
    },
###########25/04/2023

 '05CALVI3AAC': {
        'modelo' : 'COCINA',
        'cantidad':2,
        "tpn":12
    },

     '05CALVI3ABC': {
        'modelo' : 'COCINA',
        'cantidad':8,
        "tpn":13
    },

    '05R0490002AAC': {
        'modelo' : 'R490',
        'cantidad':2,
        "tpn":1.5
    },

    '05R0490002ABC': {
        'modelo' : 'R490',
        'cantidad':10,
        "tpn":7.2
    },

    '05R0490002ACC': {
        'modelo' : 'R490',
        'cantidad':10,
        "tpn":3.1
    },

     '05R0490003AAC': {
        'modelo' : 'R490',
        'cantidad':15,
        "tpn":7.4
    },


    '05R0490004AAC': {
        'modelo' : 'R490',
        'cantidad':2,
        "tpn":10
    },

     '05R0490004ABC': {
        'modelo' : 'R490',
        'cantidad':5,
        "tpn":14
    },

    '05R04900_8AAZ': {
        'modelo' : 'R490',
        'cantidad':3,
        "tpn":18
    },

    '05R04900_8ABZ': {
        'modelo' : 'R490',
        'cantidad':14,
        "tpn":3.2
    },
######################### 09/05/2023
    '05CALLR0_8AAZ': {
        'modelo' : 'COCINA',
        'cantidad':5,
        "tpn":3
    },

    '05CALLR0_8ABZ': {
        'modelo' : 'COCINA',
        'cantidad':5,
        "tpn":3
    },

      '05CALLR003ACC': {
        'modelo' : 'COCINA',
        'cantidad':82,
        "tpn":20
    },

      '05N38T0002CAC': {
        'modelo' : 'N380',
        'cantidad':1,
        "tpn":3
    },
    '05N38T0004ABC': {
        'modelo' : 'N380',
        'cantidad':10,
        "tpn":10
    },

       '05N380T003AAC': {
        'modelo' : 'N380',
        'cantidad':10,
        "tpn":11
    },
    '05N380T004AAC': {
        'modelo' : 'N380',
        'cantidad':4,
        "tpn":13
    },
    '05N380T004AAC_': {
        'modelo' : 'N380',
        'cantidad':4,
        "tpn":13
    },
        '05I800P004ACC': {
        'modelo' : 'N380',
        'cantidad':4,
        "tpn":13
    },
     '05SC360002AAC': {
        'modelo' : 'SC360',
        'cantidad':2,
        "tpn":6
    },
     '05SC3600_8AAZ': {
        'modelo' : 'SC360',
        'cantidad':24,
        "tpn":7
    },

     '05SC360002ABC': {
        'modelo' : 'SC360',
        'cantidad':39,
        "tpn":6
    },
     '05SC360004AAC': {
        'modelo' : 'SC360',
        'cantidad':2,
        "tpn":21
    },
     '05SC360003AAC': {
        'modelo' : 'SC360',
        'cantidad':11,
        "tpn":17
    },


    }


