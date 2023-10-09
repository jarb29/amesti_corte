import streamlit as st
import pandas as pd
import numpy as np
import boto3
import json
import datetime
import plotly.express as px
import datetime
from io import StringIO
from modelos import modelos_nuevos
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
    df['Modelo_Laser'] = df['Laser'].apply(lambda x: lasers[x])
    
    programas = list(set(df['Programa'].tolist()))
    missing_programs = [each for each in programas if modelos_nuevos.get(each) == None]
    print('  ')
    for pr in missing_programs:
        df = df[df["Programa"] != pr]
        
    programas_laser = list(set(df['Programa'].tolist()))
    programa_laser =  []
    
    for l in programas_laser:
        new_df = df[df['Programa'] == l]
        laser_used = list(set(new_df['Modelo_Laser'].tolist()))
        for lu in laser_used:
            if modelos_nuevos[l].get(lu) == None:
                ob_var = {
                    l:lu
                }
                programa_laser.append(ob_var)
                
    for pr in programa_laser:
        k = list(pr.keys())[0]
        df = df[df["Programa"] != k]

    df['Modelo_programas'] = df.apply(lambda x:  modelos_nuevos[x['Programa']][x['Modelo_Laser']]['modelo'], axis=1)
    df['cantidad_piezas'] = df.apply(lambda x:  modelos_nuevos[x['Programa']][x['Modelo_Laser']]['cantidad'], axis=1)
    df['Tiempo_nominal'] = df.apply(lambda x:  modelos_nuevos[x['Programa']][x['Modelo_Laser']]['tpnS'], axis=1)
    df['Desperdicio'] = df.apply(lambda x:  modelos_nuevos[x['Programa']][x['Modelo_Laser']]['dp%'], axis=1)
    print(df.head())
    return df, missing_programs, programa_laser


lasers = {
    'Laser#1': 'L5030',
    'Laser#2': 'L5030',
    'Laser#3': 'L3030',  
}

uploaded_file = st.file_uploader("Cargue el archivo")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df, missing_programs, programa_laser = total(df)
    st.write('Programas faltantes', missing_programs)
    st.write('Programas/Laser faltantes ', programa_laser)
    



# # ---- SIDEBAR ----
# st.sidebar.header("Please Filter Here:")



# sortedDates = sorted([datetime.datetime.strptime(item, '%Y-%m-%d') for item in df["date"].unique()])
# sortedDates = [item.strftime('%Y-%m-%d') for item in sortedDates]


    laser = st.sidebar.multiselect(
        "Select Laser:",
        options=df['Laser'].unique(),
        default=df['Laser'].unique()
    )

    modelos = st.sidebar.multiselect(
        "Select Modelo:",
        options=df['Modelo_programas'].unique(),
        default=df['Modelo_programas'].unique()[0:10],
    )



    df_selection = df.query(
        "Laser == @laser & Modelo_programas == @modelos "
    )

    
    programa = st.sidebar.multiselect(
        "Select Programa:",
        options=df_selection['Programa'].unique(),
        default=df_selection['Programa'].unique()[0:10],
    )
    
    df_selection_p = df_selection.query(
        "Programa == @programa"
    )
        

# # ---- MAINPAGE ----


# # TOP KPI's\
    total_tiempo = round(df["Tiempo_Bruto"].sum()/60, 2)
    date_tiempo = round(df_selection_p["Tiempo_Bruto"].sum()/60, 2)
    programas = round(df['Programa'].nunique(), 1)
    programas_selected = round(df_selection_p['Programa'].nunique(), 1)
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
        df_selection_p.groupby('Programa') \
       .agg(count=('Programa', 'size'), tiempo_promedio=('Tiempo_Bruto', 'mean'),
            tiempo_suma=('Tiempo_Bruto', 'sum')) \
       .reset_index()
       
    )

    by_product_laser = (
        df.groupby(['Programa' , 'Modelo_Laser']) \
       .agg(count=('Programa', 'size'), tiempo_promedio=('Tiempo_Bruto', 'mean'),
            tiempo_suma=('Tiempo_Bruto', 'sum')) \
       .reset_index()
       
    )
    nitrox = {
        'L5030' : 2,
        'L3030' : 4
    }
    by_product_laser['Modelo_programas'] = by_product_laser.apply(lambda x:  modelos_nuevos[x['Programa']][x['Modelo_Laser']]['modelo'], axis=1)
    by_product_laser['cantidad_piezas'] = by_product_laser.apply(lambda x:  modelos_nuevos[x['Programa']][x['Modelo_Laser']]['cantidad'], axis=1)
    by_product_laser['Tiempo_nominal'] = by_product_laser.apply(lambda x:  modelos_nuevos[x['Programa']][x['Modelo_Laser']]['tpnS'], axis=1)
    by_product_laser['Desperdicio'] = by_product_laser.apply(lambda x:  modelos_nuevos[x['Programa']][x['Modelo_Laser']]['dp%'], axis=1)
    by_product_laser['Chatarra'] = round(by_product_laser['Desperdicio'] * by_product_laser['count'] / 100, 2)
    by_product_laser['N'] = by_product_laser.apply(lambda x:  round(nitrox[x['Modelo_Laser']] * x['tiempo_suma'],2), axis=1)
    
    
    sum_chatarra = by_product_laser['Chatarra'].sum()
    sum_nitro = by_product_laser['N'].sum()
    sum_nitro_1 = by_product_laser[by_product_laser['Modelo_Laser']=='L5030']['N'].sum()
    sum_nitro_2 = by_product_laser[by_product_laser['Modelo_Laser']=='L3030']['N'].sum()
    
    plot_final = {
        'item': ['Chatarra', 'Nitro_total','Nitro_L5030','Nitro_L3030'],
        'values' : [sum_chatarra, sum_nitro, sum_nitro_1, sum_nitro_2 ]
        }
    total_df= pd.DataFrame(plot_final)
    
    
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
    
    planchas_cortadas = px.bar(
        by_product_laser,
        x=by_product_laser.Programa,
        y="count",
        color = 'Modelo_Laser',
        # orientation="h",
        title="<b>Planchas Cortdas</b>",
        # color_discrete_sequence=["#0083B8"] * len(profit_df_selection_method),
        template="plotly_dark",
        labels={'count':'Planchas Cortdas', 'Modelo_Laser':'Laser'}
        )
    planchas_cortadas.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=True))
    )
    
    
    
    
    
    best20 = px.bar(by_product_laser, y="Programa", x="count", 
                    pattern_shape="Chatarra", 
                    color = "N",
                    pattern_shape_sequence=['/', '\\', 'x', '-', '|', '+', '.'],
                    title="<b>Nitro Y Chatarra Por Programa</b>",
                    template="plotly_dark",
                    )


    best20.update_layout(
        xaxis=(dict(showgrid=True)),
        yaxis=(dict(showgrid=True)),
    )
    best20.update_coloraxes(colorbar={'orientation':'h', 'thickness':20, 'y': -1.0})

    best20.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    best20.update_yaxes(showticklabels=True)
    
    
    totales = px.bar(total_df, y="values", x="item", 
                    pattern_shape="item", 
                    color = "item",
                    pattern_shape_sequence=['/', '\\', 'x', '-', '|', '+', '.'],
                    title="<b>Nitro Y Chatarra Totales</b>",
                    template="plotly_dark",
                    )


    totales.update_layout(
        xaxis=(dict(showgrid=True)),
        yaxis=(dict(showgrid=True)),
    )
    totales.update_coloraxes(colorbar={'orientation':'h', 'thickness':20, 'y': -1.0})

    totales.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    totales.update_yaxes(showticklabels=True)
    
    

    
    
    
    

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
    st.plotly_chart(planchas_cortadas, use_container_width=True)
    st.markdown("""---""")
    st.plotly_chart(best20, use_container_width=True)
    st.markdown("""---""")
    st.plotly_chart(totales, use_container_width=True)
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


#@title
# Cantidad de pieza criticas

# Corresponde a los modelos nuevos analizados
# dp% = deperdicio en porcentaje
# tpnS = timepo nomindal en segundos
# cantidad es el numero de estufas que se pueden sacar de ese archivo en la pieza principal
# To run the model
# source .venv/bin/activate
# streamlit run Home.py
