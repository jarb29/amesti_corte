#@title
# Cantidad de pieza criticas

# Corresponde a los modelos nuevos analizados
# dp% = deperdicio en porcentaje
# tpnS = timepo nomindal en segundos
# cantidad es el numero de estufas que se pueden sacar de ese archivo en la pieza principal

modelos_nuevos = {
   '05RB050001ABC' : {
      "L5030":{
        'modelo' : 'RB',
        'cantidad':14,
        'dp%': 19.2,
        'tpnS':75,
    }
     }
   ,
    '05N0450002BBC':  {
      "L5030":{
        'modelo' : 'N450',
        'cantidad':8,
        'dp%': 4.23,
        'tpnS':68,
        },
      "L3030":{
        'modelo' : 'N450',
        'cantidad':8,
        'dp%': 4.23,
        'tpnS':71,
        }

      },



    '05RB050002AAC': {
      "L5030":{
        'modelo' : 'RB',
        'cantidad':1,
        'dp%': 29.26,
        'tpnS':100,
        }
      },


    '05N03500_8AAZ':{
      "L5030":{
        'modelo' : 'N350',
        'cantidad':24,
        'dp%': 12.79,
        'tpnS':167,
    }},


    '05N0450002BAC':{
      "L5030":{
        'modelo' : 'N450',
        'cantidad':1,
        'dp%': 31.51,
        'tpnS':150
        },
      "L3030":{
        'modelo' : 'N450',
        'cantidad':1,
        'dp%': 31.51,
        'tpnS':150
        }
      },


    '05SC380002CAC':{
      "L5030":{
        'modelo' : 'SC380',
        'cantidad':1,
        'dp%': 23.55,
        'tpnS':180
        }
      },


    '05C400B002ACC':{
      "L5030":{
        'modelo' : 'C400',
        'cantidad':5,
        'dp%': 7.03,
        'tpnS':166
        }
      },

    '05N0380002CAC':{
      "L5030":{
        'modelo' : 'N380',
        'cantidad':1,
        'dp%': 16.8,
        'tpnS':177
    }},

    '05N03800_8AAZ':{
        'modelo' : 'N380', # Falta por cuadrar
        'cantidad':14
    },

    '05RB050005AAC':{
      "L3030":{
        'modelo' : 'RB',
        'cantidad':4,
        'dp%': 6.58,
        'tpnS':295
    }},



    '05CALLR0_8ACZ':{
      "L5030":{
        'modelo' : 'COCINA',
        'cantidad':14,
        'dp%': 25.46,
        'tpnS':225
    }},

    '05R450D0_8AAZ':{
      "L5030":{
        'modelo' : 'R450D',
        'cantidad':11,
        'dp%': 18.68,
        'tpnS':225
    }},

    '05N0350002AAC':{
      "L5030":{
        'modelo' : 'N350',
        'cantidad':2,
        'dp%': 18.38,
        'tpnS':261
    }},


    '05R450D002ABC':{
      "L5030":{
        'modelo' : 'R450D',
        'cantidad':2,
        'dp%': 5.24,
        'tpnS':196
    }},

    '05Y81CH0_8ACZ':{
      "L5030":{
        'modelo' : 'I8100+',
        'cantidad':2,
        'dp%': 25.80,
        'tpnS': 289
    }},

    '05CALLR002AAC':{
      "L5030":{
        'modelo' : 'COCINA',
        'cantidad':2,
        'dp%': 22.69,
        'tpnS': 329
    }},

    '05C400B002AAC':{
      "L5030":{
        'modelo' : 'C400',
        'cantidad':4,
        'dp%': 11.94,
        'tpnS': 321
    }},

    '05C400B008AAZ':{
      "L5030":{
        'modelo' : 'C400',
        'cantidad':10,
        'dp%': 11.12,
        'tpnS': 209
    }},

    '05Y81CH0_8ABZ':{
      "L5030":{
        'modelo' : 'I8100+',
        'cantidad':2,
        'dp%': 34.86,
        'tpnS': 379
    }},

    '05C400B002ABC':{
      "L5030":{
        'modelo' : 'C400',
        'cantidad':14,
        'dp%': 10.54,
        'tpnS': 329
        }
      },

    '05N0450003AAC':{
      "L5030":{
        'modelo' : 'N450',
        'cantidad':10,
        'dp%': 16.55,
        'tpnS': 534
        },
      "L3030":{
        'modelo' : 'N450',
        'cantidad':10,
        'dp%': 16.55,
        'tpnS': 480
        },

      },

    '05Y81CH002AAC':{
      "L5030":{
        'modelo' : 'I8100+',
        'cantidad':1,
        'dp%': 30.12,
        'tpnS': 454
        },
      "L3030":{
        'modelo' : 'I8100+',
        'cantidad':1,
        'dp%': 30.12,
        'tpnS': 454
        }
      },

    '05R450D002AAC':{
      "L5030":{
        'modelo' : 'R450D',
        'cantidad':8,
        'dp%': 17.65,
        'tpnS': 459
        },

      },

    '05R450D003ABC':{
      "L5030":{
        'modelo' : 'R450D',
        'cantidad':4,
        'dp%': 33.06,
        'tpnS': 373
        },
      "L3030":{
        'modelo' : 'R450D',
        'cantidad':4,
        'dp%': 33.06,
        'tpnS': 400
        }
      },



    '05N0380003AAC':{
      "L5030":{ # Modelo sin templador
        'modelo' : 'N380',
        'cantidad':32,
        'dp%': 11.42,
        'tpnS': 720
        },
      "L3030":{ # Modelo con templador
        'modelo' : 'N380',
        'cantidad':10,
        'dp%': 18.94,
        'tpnS': 610
        }
      },


    '05RB050004AAC':{
      "L5030":{
        'modelo' : 'RB',
        'cantidad':4,
        'dp%': 3.7,
        'tpnS': 482
        }, # Los archivos son diferentes en los archivos de pdf
      "L3030":{
        'modelo' : 'RB',
        'cantidad':5,
        'dp%': 40.65,
        'tpnS': 550
        }
      },


    '05R450D003AAC':{
      "L5030":{
        'modelo' : 'R450D',
        'cantidad':6,
        'dp%': 33.25,
        'tpnS': 546
        },
      "L3030":{
        'modelo' : 'R450D',
        'cantidad':6,
        'dp%': 33.25,
        'tpnS': 605
        }
      },



    '05RB050003AAC':{
      "L5030":{
        'modelo' : 'RB',
        'cantidad':10,
        'dp%': 13.11,
        'tpnS': 769
        },
      "L3030":{
        'modelo' : 'RB',
        'cantidad':10,
        'dp%': 13.11,
        'tpnS': 759
        }
      },

    '05RB050004ABC':{
      "L5030":{
        'modelo' : 'RB',
        'cantidad':5,
        'dp%': 41.67,
        'tpnS': 819
        },
      "L3030":{ # Los programas de corte son diferentes
        'modelo' : 'RB',
        'cantidad':4,
        'dp%': 3.70,
        'tpnS': 313

        }
      },

###########################################
###########################################

    '05N0350003AAC':{
      "L5030":{
        'modelo' : 'N350',
        'cantidad':14,
        'dp%': 24.23,
        'tpnS': 699
        },
      "L3030":{
        'modelo' : 'N350',
        'cantidad':14,
        'dp%': 24.23,
        'tpnS': 647
        }
      },


    '05Y81CH0_8AAZ':{
      "L5030":{
        'modelo' : 'I8100+',
        'cantidad':4,
        'dp%': 29.26,
        'tpnS': 633
        },
      },

    '05N0450004AAC':{
      "L5030":{
        'modelo' : 'N450',
        'cantidad':2,
        'dp%': 21.27,
        'tpnS': 769
        },
      "L3030":{
        'modelo' : 'N450',
        'cantidad':2,
        'dp%': 22.02,
        'tpnS': 528
        }
      },

    '05N0380004AAC':{
      "L3030":{
        'modelo' : 'N380',
        'cantidad':2,
        'dp%': 17.34,
        'tpnS': 701
        }
      },


    '05N0350004AAC':{
      "L5030":{
        'modelo' : 'N350',
        'cantidad':4,
        'dp%': 14.38,
        'tpnS': 1350
        },
      "L3030":{
        'modelo' : 'N350',
        'cantidad':4,
        'dp%': 14.38,
        'tpnS': 878
        }
      },

    '05N0380004ABC':{
      "L5030":{
        'modelo' : 'N380',
        'cantidad':10,
        'dp%': 11.92,
        'tpnS': 566
        }
      },

    '05C400B003ABC':{
      "L5030":{
        'modelo' : 'C400',
        'cantidad':21,
        'dp%': 20.71,
        'tpnS': 712
        },
      "L3030":{
        'modelo' : 'C400',
        'cantidad':21,
        'dp%': 20.71,
        'tpnS': 604
        }
      },


    '05CALVI1_5AAI':{
      "L3030":{
        'modelo' : 'COCINA',
        'cantidad':4,
        'dp%': 17.25,
        'tpnS': 551
        },
      "L5030":{
        'modelo' : 'COCINA',
        'cantidad':4,
        'dp%': 17.25,
        'tpnS': 579
        }
      },

    '05C400B003AAC':{
      "L5030":{
        'modelo' : 'C400',
        'cantidad':3,
        'dp%': 18.96,
        'tpnS': 543
        },
      "L3030":{
        'modelo' : 'C400',
        'cantidad':3,
        'dp%': 18.96,
        'tpnS': 511
        }
      },
    '05N0450004ABC':{
      "L5030":{
        'modelo' : 'N450',
        'cantidad':8,
        'dp%': 12.98,
        'tpnS': 727
        },
      "L3030":{
        'modelo' : 'N450',
        'cantidad':8,
        'dp%': 12.98,
        'tpnS': 771
        }
      },


    '05R450D004AAC':{
      "L5030":{
        'modelo' : 'R450D',
        'cantidad':4,
        'dp%': 29.67,
        'tpnS': 1252
        },
      "L3030":{
        'modelo' : 'R450D',
        'cantidad':4,
        'dp%': 29.67,
        'tpnS': 806
        }
      },

    '05C400B004AAC':{
       "L3030":{
          'modelo' : 'C400',
          'cantidad':2,
          'dp%': 12.37,
          'tpnS': 780
        },
        "L5030":{
          'modelo' : 'C400',
          'cantidad':2,
          'dp%': 12.37,
          'tpnS': 1096
        }
      },


    '05SC380004AAC':{
       "L5030":{
        'modelo' : 'SC380',
        'cantidad':2,
        'dp%': 12.76,
        'tpnS': 962
        },
        "L3030":{
        'modelo' : 'SC380',
        'cantidad':2,
        'dp%': 12.76,
        'tpnS': 685
        },
       },

    '05Y81CH004AAC':{
       "L3030":{
        'modelo' : 'I8100+',
        'cantidad':6,
        'dp%': 20.80,
        'tpnS': 1386
        }
       },
    '05RB050005ABC':{
       "L3030":{
        'modelo' : 'RB',
        'cantidad':4,
        'dp%': 21.84,
        'tpnS': 1218
        }
       },


    '05N0450004ACC':{
       "L5030":{
        'modelo' : 'N450',
        'cantidad':16,
        'dp%': 17.21,
        'tpnS': 1566
        },
      "L3030":{
        'modelo' : 'N450',
        'cantidad':16,
        'dp%': 18.03,
        'tpnS': 799
        }
       },


    '05CALLR006AAC':{
       "L3030":{
          'modelo' : 'COCINA',
          'cantidad':6,
          'dp%': 21.22,
          'tpnS': 1418
          },
        "L5030":{
            'modelo' : 'COCINA',
            'cantidad':6,
            'dp%': 21.22,
            'tpnS': 2519
          }
       },

    '05Y81CH003AAI': {
       "L3030":{
        'modelo' : 'I8100+',
        'cantidad':42,
        'dp%': 41.03,
        'tpnS': 3909
        }
       },

    ##############
    "ESP_DEFLECT0R_3MM":{
       "L3030":{
        'modelo' : 'N350',
        'cantidad':15,
        'dp%': 1,
        'tpnS': 420
        }
       },

      "REJILLA_3MM_2000":{
       "L5030":{
        'modelo' : 'FLEJES',
        'cantidad':9,
        "tpn":1260
        }
       },

        "05SC380002AAC_BM":{
            "L5030":{
        'modelo' : 'SC380',
        'cantidad':1,
        'dp%': 23.35,
        'tpnS': 180
        }
       },

        "05I800P002ABC":{
            "L5030":{
        'modelo' : 'INSERTO3',
        'cantidad':3,
        'dp%': 17.74,
        'tpnS': 302
        }
            },

        "05S380T003AAC":{
            "L5030":{
        'modelo' : 'SC380',
        'cantidad':11,
        'dp%': 15.54,
        'tpnS': 300
        }
            },

        "05I800P006AAC":{
            "L5030":{
        'modelo' : 'INSERTO3',
        'cantidad':12,
        'dp%': 20.81,
        'tpnS': 1682
    }},

# Corresponde  a modelos que se cortaron pero con la nomenclatura vieja


      'CAIN0X2_C0NJ_4MM':{
          "L3030":{
              'modelo' : 'COCINA',
              'cantidad':12,
              'dp%': 14.12,
              'tpnS': 1397
              }
            },

      'CAIN0X2_C0NJII_3':{
          "L5030":{
              'modelo' : 'COCINA',
              'cantidad':8,
              'dp%': 15.53,
              'tpnS': 827
              },
          "L3030":{
              'modelo' : 'COCINA',
              'cantidad':8,
              'dp%': 15.53,
              'tpnS': 780
              }
          },

      'CAIN0X2_C0NJI_3MM':{
          "L5030":{
              'modelo' : 'COCINA',
              'cantidad':2,
              'dp%': 15.89,
              'tpnS': 751
          },
          "L3030":{
              'modelo' : 'COCINA',
              'cantidad':2,
              'dp%': 15.89,
              'tpnS': 661
          }
    },


      'CAIN0X2_C0NJ_05MM':{
          "L5030":{
              'modelo' : 'COCINA',
              'cantidad':1,
              'dp%': 10.67,
              'tpnS': 138
              }
          },


    'I8100P_1_PAN_C400':{
          "L5030":{
              'modelo' : 'I8100+',
              'cantidad':2,
              'dp%': 20.81,
              'tpnS': 244
              }
          },

    '05C500B002AAC':{
        "L5030":{
            'modelo' : 'C500',
            'cantidad':3,
            'dp%': 11.67,
            'tpnS': 159
            }
        },

    '05C500B002ABC':{
        "L5030":{
            'modelo' : 'C500',
            'cantidad':2,
            'dp%': 15.22,
            'tpnS': 321
            }
        },

    '05C500B003AAC':{
        "L5030":{
          'modelo' : 'C500',
          'cantidad':5,
          'dp%': 28.91,
          'tpnS': 540
          },
        "L3030":{
          'modelo' : 'C500',
          'cantidad':5,
          'dp%': 28.91,
          'tpnS': 500
          }
        },


    '05C500B004AAC':{
        "L5030":{
          'modelo' : 'C500',
          'cantidad':2,
          'dp%': 11.06,
          'tpnS': 1030
        },
      "L3030":{
          'modelo' : 'C500',
          'cantidad':2,
          'dp%': 11.94,
          'tpnS': 1022
        }
    },

# Corresponde a los modelos que tienen el nuevo nombre pero no se pudieron analizar

    '05RB050001AAC':{
        "L5030":{
          'modelo' : 'RB',
          'cantidad':14,
          'dp%': 7.3,
          'tpnS': 88
        }
    },



    '05SC3800_8AAZ':{
        "L5030":{
          'modelo' : 'SC380',
          'cantidad':14,
          'dp%': 22.89,
          'tpnS': 77
          }
        },


    '05N0380002AAC':{
        "L5030":{
          'modelo' : 'N380',
          'cantidad':1,
          'dp%': 11.06,
          'tpnS': 196
          }
        },

    '05C400B0_8ABZ':{
        "L5030":{
          'modelo' : 'C400',
          'cantidad':3,
          'dp%': 12.79,
          'tpnS': 94
        }
        },

    '05I800P004ABC': {
        "L5030":{
          'modelo' : 'INSERTO3',
          'cantidad':3,
          'dp%': 18.38,
          'tpnS': 854
        },
        "L3030":{
          'modelo' : 'INSERTO3',
          'cantidad':3,
          'dp%': 18.44,
          'tpnS': 667
        }
    },



    '05I800P002AAC':  {
        "L5030":{
          'modelo' : 'INSERTO3',
          'cantidad':2,
          'dp%': 22.45,
          'tpnS': 358
          }
        },


    '05CALVI4AAI': {
        "L5030":{
          'modelo' : 'COCINA',
          'cantidad':22,
          'dp%': 16.03,
          'tpnS': 849
        }
    },


    '05I800P004AAC': {
        "L5030":{
          'modelo' : 'INSERTO3',
          'cantidad':2,
          'dp%': 13.13,
          'tpnS': 832
        }
    },

   #########################################################################
   #########################################################################


    '05N0350004ABC': {
        "L5030":{
          'modelo' : 'N350',
          'cantidad':6,
          'dp%': 15.28,
          'tpnS': 1079
        },
        "L3030":{
          'modelo' : 'N350',
          'cantidad':6,
          'dp%': 15.28,
          'tpnS': 681
        }
        },
    '05I800P003AAC': {
        "L5030":{
          'modelo' : 'INSERTO3',
          'cantidad':8,
          'dp%': 21.08,
          'tpnS': 713
        },
      "L3030":{
          'modelo' : 'INSERTO3',
          'cantidad':8,
          'dp%': 21.08,
          'tpnS': 724
        }
    },

    "CAIN0X2_C0NJ_6MM":  {
        "L3030":{
            'modelo' : 'COCINA',
            'cantidad':6,
            'dp%': 21.22,
            'tpnS': 1418
          },
        "L5030":{
            'modelo' : 'COCINA',
            'cantidad':6,
            'dp%': 21.22,
            'tpnS': 2419
        },
    },

    "05I800P001AAC": {
        "L5030":{
          'modelo' : 'INSERTO3',
          'cantidad':36,
          'dp%': 13.19,
          'tpnS': 935
        }
    },

    "05N0360003AAC": {
        "L5030":{
          'modelo' : 'N3604',
          'cantidad':11,
          'dp%': 16.61,
          'tpnS': 714
        },
        "L3030":{
          'modelo' : 'N3604',
          'cantidad':11,
          'dp%': 16.61,
          'tpnS': 650
        }
    },

    "05N0360002AAC": {
        "L5030":{
          'modelo' : 'N3604',
          'cantidad':2,
          'dp%': 13.82,
          'tpnS': 251
        }
    },
    "05N0360004AAC": {
        "L5030":{
            'modelo' : 'N3604',
            'cantidad':2,
            'dp%': 20.68,
            'tpnS': 1059
          },
        "L3030":{
            'modelo' : 'N3604',
            'cantidad':2,
            'dp%': 20.68,
            'tpnS': 858
          }
    },

    "05N03600_8AAZ": {
        "L5030":{
          'modelo' : 'N3604',
          'cantidad':24,
            'dp%': 14.21,
            'tpnS': 134
        }
    },

     "05RB0500_8AAC":  {
        "L5030":{
          'modelo' : 'RB',
          'cantidad':21,
          'dp%': 7.3,
          'tpnS': 88
        }
    },

     "05RB0500_8ABC": {
        "L5030":{
          'modelo' : 'RB',
          'cantidad':14,
          'dp%': 19.2,
          'tpnS': 49
        }
    },

###########25/04/2023

 '05CALVI3AAC': {
        "L5030":{
          'modelo' : 'COCINA',
          'cantidad':2,
          'dp%': 14.53,
          'tpnS': 901
        },
        "L3030":{
          'modelo' : 'COCINA',
          'cantidad':2,
          'dp%': 14.53,
          'tpnS': 730
        }
    },

     '05CALVI3ABC':  {
        "L5030":{
          'modelo' : 'COCINA',
          'cantidad':8,
          'dp%': 17.03,
          'tpnS': 931
        },
        "L3030":{
          'modelo' : 'COCINA',
          'cantidad':8,
          'dp%': 17.03,
          'tpnS': 718
        }
    },


    '05R0490002AAC': {
        "L5030":{
          'modelo' : 'R490',
          'cantidad':2,
          'dp%': 8.72,
          'tpnS': 136
        }
    },

    '05R0490002ABC': {
        "L5030":{
          'modelo' : 'R490',
          'cantidad':10,
          'dp%': 15.84,
          'tpnS': 431
        }
    },

    '05R0490002ACC': {
        "L5030":{
          'modelo' : 'R490',
          'cantidad':10,
          'dp%': 17.62,
          'tpnS': 192
        }
    },

     '05R0490003AAC':  {
        "L5030":{
          'modelo' : 'R490',
          'cantidad':15,
          'dp%': 6.15,
          'tpnS': 612
        }
    },

    '05R0490004AAC': {
        "L5030":{
          'modelo' : 'R490',
          'cantidad':2,
          'dp%': 13.80,
          'tpnS': 796
        },
        "L3030":{
          'modelo' : 'R490',
          'cantidad':2,
          'dp%': 13.80,
          'tpnS': 628
        }
    },

     '05R0490004ABC':  {
        "L5030":{
          'modelo' : 'R490',
          'cantidad':5,
          'dp%': 34.29,
          'tpnS': 1246
        },
        "L3030":{
          'modelo' : 'R490',
          'cantidad':5,
          'dp%': 34.29,
          'tpnS': 850
        }
    },

    '05R04900_8AAZ': {
        "L5030":{
          'modelo' : 'R490',
          'cantidad':3,
          'dp%': 14.12,
          'tpnS': 166
        }
    },

    '05R04900_8ABZ': {
        "L5030":{
          'modelo' : 'R490',
          'cantidad':14,
          'dp%': 19.89,
          'tpnS': 210
        }
    },

######################### 09/05/2023
    '05CALLR0_8AAZ': {
        "L5030":{
          'modelo' : 'COCINA',
          'cantidad':5,
          'dp%': 10.12,
          'tpnS': 169
        }
    },

    '05CALLR0_8ABZ': {
        "L5030":{
          'modelo' : 'COCINA',
          'cantidad':5,
          'dp%': 15.7,
          'tpnS': 118
        }
    },

      '05CALLR003ACC':  {
        "L5030":{
          'modelo' : 'COCINA',
          'cantidad':82,
          'dp%': 15.29,
          'tpnS': 1213
        },
        "L3030":{
          'modelo' : 'COCINA',
          'cantidad':82,
          'dp%': 15.29,
          'tpnS': 1120
        }
    },

      '05N38T0002CAC': {
        "L5030":{
          'modelo' : 'N380',
          'cantidad':1,
          'dp%': 16.80,
          'tpnS': 177
        }
    },

    '05N38T0004ABC': {
        "L3030":{
          'modelo' : 'N380',
          'cantidad':10,
          'dp%': 11.92,
          'tpnS': 566
        }
    },

     '05SC360002AAC':  {
        "L5030":{
          'modelo' : 'SC360',
          'cantidad':2,
          'dp%': 16.21,
          'tpnS': 334
        },
        "L3030":{
          'modelo' : 'SC360',
          'cantidad':2,
          'dp%': 16.21,
          'tpnS': 434
        }
    },

     '05SC3600_8AAZ':  {
        "L5030":{
          'modelo' : 'SC360',
          'cantidad':24,
          'dp%': 8.25,
          'tpnS': 379
        }
    },

     '05SC360002ABC': {
        "L5030":{
          'modelo' : 'SC360',
          'cantidad':39,
          'dp%': 5.45,
          'tpnS': 333
        }
    },
     '05SC360004AAC': {
        "L5030":{
          'modelo' : 'SC360',
          'cantidad':2,
          'dp%': 18.45,
          'tpnS': 1241
        },
        "L3030":{
          'modelo' : 'SC360',
          'cantidad':2,
          'dp%': 18.45,
          'tpnS': 884
        }
    },
     '05SC360003AAC': {
        "L5030":{
          'modelo' : 'SC360',
          'cantidad':11,
          'dp%': 14.47,
          'tpnS': 1003
        },

      "L3030":{
          'modelo' : 'SC360',
          'cantidad':11,
          'dp%': 14.47,
          'tpnS': 799
        }
    },

    '05RBO50005AAC': {
      "L3030":{
          'modelo' : 'RB',
          'cantidad':4,
          'dp%': 6.54,
          'tpnS': 300
        }
    },
   "05CO650002AAC": {
      "L5030":{
          'modelo' : 'C650',
          'cantidad':4,
          'dp%': 13.26,
          'tpnS': 228
        },
      "L3030":{
          'modelo' : 'C650',
          'cantidad':4,
          'dp%': 13.26,
          'tpnS': 266
        }
    },
   "05CALVI1_5ABI": {
      "L5030":{
          'modelo' : 'COCINA',
          'cantidad':4,
          'dp%': 17.25,
          'tpnS': 579
        },
      "L3030":{
          'modelo' : 'COCINA',
          'cantidad':22,
          'dp%': 39.42,
          'tpnS': 600
        }
    },
   "05RO490002AAC": {
      "L5030":{
          'modelo' : 'R490',
          'cantidad':2,
          'dp%': 8.72,
          'tpnS': 136
        }
    },
   "05CO650004AAC": {
      "L5030":{
          'modelo' : 'C650',
          'cantidad':4,
          'dp%': 25.65,
          'tpnS': 992
        }
    },
   "05CO650004AAC": {
      "L5030":{
          'modelo' : 'C650',
          'cantidad':4,
          'dp%': 25.65,
          'tpnS': 992
        }
    },

   "05SC350003AAC": {
      "L5030":{
          'modelo' : 'SC350',
          'cantidad':14,
          'dp%': 24.23,
          'tpnS': 754
        },
      "L3030":{
          'modelo' : 'SC350',
          'cantidad':14,
          'dp%': 24.26,
          'tpnS': 721
        }
    },
   "05RBO50004ABC": {
      "L3030":{
          'modelo' : 'RB',
          'cantidad':4,
          'dp%': 3.7,
          'tpnS': 313
        }
    },
   "05RBO50005ABC": {
      "L3030":{
          'modelo' : 'RB',
          'cantidad':4,
          'dp%': 21.24,
          'tpnS': 801
        }
    },
   "05SC350004AAC": {
      "L3030":{
          'modelo' : 'SC350',
          'cantidad':4,
          'dp%': 21.62,
          'tpnS': 841
        },
      "L5030":{
          'modelo' : 'SC350',
          'cantidad':4,
          'dp%': 18.53,
          'tpnS': 1075
        }
    },
   "05SC350004ABC": {
      "L3030":{
          'modelo' : 'SC350',
          'cantidad':5,
          'dp%': 10.53,
          'tpnS': 690
        },
      "L5030":{
          'modelo' : 'SC350',
          'cantidad':5,
          'dp%': 10.53,
          'tpnS': 1105
        }
    },

   ####################################################
      "05CALVI0_8AAZ": {
      "L5030":{
          'modelo' : 'COCINA',
          'cantidad':5,
          'dp%': 10.12,
          'tpnS': 160
        }
    },

    "05CALVI004AAC": {
      "L3030":{
          'modelo' : 'COCINA',
          'cantidad':12,
          'dp%': 13.25,
          'tpnS': 310
        }
    },

    "05RO4900_8ABZ": {
      "L5030":{
          'modelo' : 'R490',
          'cantidad':14,
          'dp%': 19.89,
          'tpnS': 210
        }
    },

   "05RBO50001AAC": {
      "L5030":{
          'modelo' : 'RB',
          'cantidad':14,
          'dp%': 19.89,
          'tpnS': 210
        }
    },
   "05RBO50001ABC": {
      "L5030":{
          'modelo' : 'RB',
          'cantidad':14,
          'dp%': 19.20,
          'tpnS': 75
        }
    },
   "05SC350002AAC": {
      "L5030":{
          'modelo' : 'SC350',
          'cantidad':2,
          'dp%': 17.96,
          'tpnS': 253
        }
    },

    }


