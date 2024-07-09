COMMODITY_KEY = "NATURALGAS" # Always all caps

COMMODITY_TO_PRICE_FILE_MAP = {
    "GOLD": "GoldPrices.csv",
    "COPPER": "CopperPrices.csv",
    "CRUDEOIL": "CrudeOilPrices.csv",
    "NATURALGAS": "NaturalGasPrices.csv",
}

COMMODITY_TO_COT_NAMES_MAP = {
    "GOLD": ["GOLD - COMMODITY EXCHANGE INC."],
    "COPPER": ["COPPER-GRADE #1 - COMMODITY EXCHANGE INC.",
               "COPPER- #1 - COMMODITY EXCHANGE INC."],
    "CRUDEOIL": [""],
    "NATURALGAS": ["NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE",
                   "NATURAL GAS - NEW YORK MERCANTILE EXCHANGE"],
}

# Set flag to determine what features to use in the model
COMMODITY_TO_FEATURE_PROFILES_MAP = {

    "GOLD": {
        # Technicals
        'RSI': 1,
        'MACD': 1,
        'Signal Line': 1,
        'Upper Band': 0,
        'Lower Band' : 0,
        'RSI_LONG': 1,
        'BIG MACD': 0,
        'BIG Signal Line': 0,

        # Currencies
        'CloseDXY': 0,
        'CloseCHINA': 0,
        'CloseRUSSIA': 0,
        'CloseAUS': 0,
        'CloseCANADA': 0,

        # Indexes
        'CloseVIX': 0,
        'CloseDXY': 0,

        # COT Data
        'Pct_of_OI_Prod_Merc_Long_All': 0,
        'Pct_of_OI_Prod_Merc_Short_All': 0,
        'Pct_of_OI_M_Money_Long_All': 0,
        'Pct_of_OI_M_Money_Short_All': 0,
        'Pct_of_OI_M_Money_Spread_All': 0,
        'Pct_of_OI_Swap_Long_All': 0,
        'Pct_of_OI_Swap_Short_All': 0,
        'Pct_of_OI_Swap_Spread_All': 0,
        'Pct_of_OI_Other_Rept_Long_All': 0,
        'Pct_of_OI_Other_Rept_Short_All': 0,
        'Pct_of_OI_Other_Rept_Spread_All': 0,

        'Percent_PMPU_Long': 0,
        'Percent_PMPU_Short': 0,
        'Percent_MM_Long': 0,
        'Percent_MM_Short': 0,
        'Percent_MM_Spread': 0,
        'Percent_SWAP_Long': 0,
        'Percent_SWAP_Short': 0,
        'Percent_SWAP_Spread': 0,
        'Percent_OR_Long': 0,
        'Percent_OR_Short': 0,
        'Percent_OR_Spread': 0,

        'Open_Interest_All': 0,
        'Prod_Merc_Positions_Long_ALL': 0,
        'Prod_Merc_Positions_Short_ALL': 0,
        'M_Money_Positions_Long_ALL': 0,
        'M_Money_Positions_Short_ALL': 0,
        'M_Money_Positions_Spread_ALL': 0,
        'Swap_Positions_Long_All': 0,
        'Swap__Positions_Short_All': 0,
        'Swap__Positions_Spread_All': 0,
        'Other_Rept_Positions_Long_ALL': 0,
        'Other_Rept_Positions_Short_ALL': 0,
        'Other_Rept_Positions_Spread_ALL': 0,

        'Change_in_Open_Interest_All': 0,
        'Change_in_Prod_Merc_Long_All': 1,
        'Change_in_Prod_Merc_Short_All': 0,
        'Change_in_M_Money_Long_All': 1,
        'Change_in_M_Money_Short_All': 0,
        'Change_in_M_Money_Spread_All': 0,
        'Change_in_Swap_Long_All': 0,
        'Change_in_Swap_Short_All': 0,
        'Change_in_Swap_Spread_All': 0,
        'Change_in_Other_Rept_Long_All': 0,
        'Change_in_Other_Rept_Short_All': 0,
        'Change_in_Other_Rept_Spread_All': 0},


    "COPPER": {
        # Technicals
        'RSI': 1,
        'MACD': 1,
        'Signal Line': 1,
        'Upper Band': 0,
        'Lower Band' : 0,
        'RSI_LONG': 1,

        # Currencies
        'CloseDXY': 0,
        'CloseCHINA': 0,
        'CloseRUSSIA': 0,
        'CloseAUS': 0,
        'CloseCANADA': 0,

        # Indexes
        'CloseVIX': 0,
        'CloseDXY': 0,

        # COT Data
        'Pct_of_OI_Prod_Merc_Long_All': 0,
        'Pct_of_OI_Prod_Merc_Short_All': 0,
        'Pct_of_OI_M_Money_Long_All': 0,
        'Pct_of_OI_M_Money_Short_All': 0,
        'Pct_of_OI_M_Money_Spread_All': 0,
        'Pct_of_OI_Swap_Long_All': 0,
        'Pct_of_OI_Swap_Short_All': 0,
        'Pct_of_OI_Swap_Spread_All': 0,
        'Pct_of_OI_Other_Rept_Long_All': 0,
        'Pct_of_OI_Other_Rept_Short_All': 0,
        'Pct_of_OI_Other_Rept_Spread_All': 0,

        'Percent_PMPU_Long': 0,
        'Percent_PMPU_Short': 0,
        'Percent_MM_Long': 0,
        'Percent_MM_Short': 0,
        'Percent_MM_Spread': 0,
        'Percent_SWAP_Long': 1,
        'Percent_SWAP_Short': 1,
        'Percent_SWAP_Spread': 0,
        'Percent_OR_Long': 0,
        'Percent_OR_Short': 0,
        'Percent_OR_Spread': 0,

        'Open_Interest_All': 0,
        'Prod_Merc_Positions_Long_ALL': 0,
        'Prod_Merc_Positions_Short_ALL': 0,
        'M_Money_Positions_Long_ALL': 0,
        'M_Money_Positions_Short_ALL': 0,
        'M_Money_Positions_Spread_ALL': 0,
        'Swap_Positions_Long_All': 0,
        'Swap__Positions_Short_All': 0,
        'Swap__Positions_Spread_All': 0,
        'Other_Rept_Positions_Long_ALL': 0,
        'Other_Rept_Positions_Short_ALL': 0,
        'Other_Rept_Positions_Spread_ALL': 0,

        'Change_in_Open_Interest_All': 0,
        'Change_in_Prod_Merc_Long_All': 1,
        'Change_in_Prod_Merc_Short_All': 1,
        'Change_in_M_Money_Long_All': 1,
        'Change_in_M_Money_Short_All': 1,
        'Change_in_M_Money_Spread_All': 1,
        'Change_in_Swap_Long_All': 0,
        'Change_in_Swap_Short_All': 0,
        'Change_in_Swap_Spread_All': 0,
        'Change_in_Other_Rept_Long_All': 0,
        'Change_in_Other_Rept_Short_All': 0,
        'Change_in_Other_Rept_Spread_All': 0},

    "CRUDEOIL": {
        # Technicals
        'RSI': 1,
        'MACD': 1,
        'Signal Line': 1,
        'Upper Band': 1,
        'Lower Band' : 1,
        'RSI_LONG': 1,

        # Currencies
        'CloseDXY': 1,
        'CloseCHINA': 1,
        'CloseRUSSIA': 1,
        'CloseAUS': 1,
        'CloseCANADA': 1,

        # Indexes
        'CloseVIX': 1,
        'CloseDXY': 1,

        # COT Data
        'Pct_of_OI_Prod_Merc_Long_All': 1,
        'Pct_of_OI_Prod_Merc_Short_All': 1,
        'Pct_of_OI_M_Money_Long_All': 1,
        'Pct_of_OI_M_Money_Short_All': 1,
        'Pct_of_OI_M_Money_Spread_All': 1,
        'Pct_of_OI_Swap_Long_All': 1,
        'Pct_of_OI_Swap_Short_All': 1,
        'Pct_of_OI_Swap_Spread_All': 1,
        'Pct_of_OI_Other_Rept_Long_All': 1,
        'Pct_of_OI_Other_Rept_Short_All': 1,
        'Pct_of_OI_Other_Rept_Spread_All': 1,

        'Percent_PMPU_Long': 1,
        'Percent_PMPU_Short': 1,
        'Percent_MM_Long': 1,
        'Percent_MM_Short': 1,
        'Percent_MM_Spread': 1,
        'Percent_SWAP_Long': 1,
        'Percent_SWAP_Short': 1,
        'Percent_SWAP_Spread': 1,
        'Percent_OR_Long': 1,
        'Percent_OR_Short': 1,
        'Percent_OR_Spread': 1,

        'Open_Interest_All': 1,
        'Prod_Merc_Positions_Long_ALL': 1,
        'Prod_Merc_Positions_Short_ALL': 1,
        'M_Money_Positions_Long_ALL': 1,
        'M_Money_Positions_Short_ALL': 1,
        'M_Money_Positions_Spread_ALL': 1,
        'Swap_Positions_Long_All': 1,
        'Swap__Positions_Short_All': 1,
        'Swap__Positions_Spread_All': 1,
        'Other_Rept_Positions_Long_ALL': 1,
        'Other_Rept_Positions_Short_ALL': 1,
        'Other_Rept_Positions_Spread_ALL': 1,

        'Change_in_Open_Interest_All': 1,
        'Change_in_Prod_Merc_Long_All': 1,
        'Change_in_Prod_Merc_Short_All': 0,
        'Change_in_M_Money_Long_All': 1,
        'Change_in_M_Money_Short_All': 0,
        'Change_in_M_Money_Spread_All': 1,
        'Change_in_Swap_Long_All': 1,
        'Change_in_Swap_Short_All': 0,
        'Change_in_Swap_Spread_All': 1,
        'Change_in_Other_Rept_Long_All': 1,
        'Change_in_Other_Rept_Short_All': 0,
        'Change_in_Other_Rept_Spread_All': 1},

    "NATURALGAS": {
        # Technicals
        'RSI': 1,
        'MACD': 1,
        'Signal Line': 1,
        'Upper Band': 0,
        'Lower Band' : 0,
        'RSI_LONG': 1,

        # Currencies
        'CloseDXY': 0,
        'CloseCHINA': 0,
        'CloseRUSSIA': 0,
        'CloseAUS': 0,
        'CloseCANADA': 0,

        # Indexes
        'CloseVIX': 0,
        'CloseDXY': 0,

        # COT Data
        'Pct_of_OI_Prod_Merc_Long_All': 0,
        'Pct_of_OI_Prod_Merc_Short_All': 0,
        'Pct_of_OI_M_Money_Long_All': 0,
        'Pct_of_OI_M_Money_Short_All': 0,
        'Pct_of_OI_M_Money_Spread_All': 0,
        'Pct_of_OI_Swap_Long_All': 0,
        'Pct_of_OI_Swap_Short_All': 0,
        'Pct_of_OI_Swap_Spread_All': 0,
        'Pct_of_OI_Other_Rept_Long_All': 0,
        'Pct_of_OI_Other_Rept_Short_All': 0,
        'Pct_of_OI_Other_Rept_Spread_All': 0,

        'Percent_PMPU_Long': 0,
        'Percent_PMPU_Short': 0,
        'Percent_MM_Long': 0,
        'Percent_MM_Short': 0,
        'Percent_MM_Spread': 0,
        'Percent_SWAP_Long': 1,
        'Percent_SWAP_Short': 0,
        'Percent_SWAP_Spread': 0,
        'Percent_OR_Long': 0,
        'Percent_OR_Short': 0,
        'Percent_OR_Spread': 0,

        'Open_Interest_All': 0,
        'Prod_Merc_Positions_Long_ALL': 0,
        'Prod_Merc_Positions_Short_ALL': 0,
        'M_Money_Positions_Long_ALL': 0,
        'M_Money_Positions_Short_ALL': 0,
        'M_Money_Positions_Spread_ALL': 0,
        'Swap_Positions_Long_All': 0,
        'Swap__Positions_Short_All': 0,
        'Swap__Positions_Spread_All': 0,
        'Other_Rept_Positions_Long_ALL': 0,
        'Other_Rept_Positions_Short_ALL': 0,
        'Other_Rept_Positions_Spread_ALL': 0,

        'Change_in_Open_Interest_All': 0,
        'Change_in_Prod_Merc_Long_All': 1,
        'Change_in_Prod_Merc_Short_All': 0,
        'Change_in_M_Money_Long_All': 1,
        'Change_in_M_Money_Short_All': 0,
        'Change_in_M_Money_Spread_All': 1,
        'Change_in_Swap_Long_All': 1,
        'Change_in_Swap_Short_All': 0,
        'Change_in_Swap_Spread_All': 1,
        'Change_in_Other_Rept_Long_All': 1,
        'Change_in_Other_Rept_Short_All': 0,
        'Change_in_Other_Rept_Spread_All': 1}

}
