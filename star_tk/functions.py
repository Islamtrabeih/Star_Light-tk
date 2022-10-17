import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math, sys, os
from datetime import datetime, timedelta
from star_tk.smoothing import *
from star_tk.groundtrack import *


# main functions
# ----------------------------------------------------------------------------------------------------------------------

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def data_sheets(height, yy, mm, xx, season, itr):
    prop = ["Argon", "Density", "Temperature", "Atomic Oxygen", "Oxygen", "Atomic Nitrogen", "Nitrogen", "Helium", "Hydrogen"]
    at = pd.read_csv(resource_path(f'star_tk/data/{xx}.csv'), header = None)
    x = [[], []]
    yy, mm = int(yy), int(mm)
    rr = (yy - 1996) * 12 + mm + 1
    if rr < at.index[-1]:                                                     # append data and date to list x
        for i in range(1, rr, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%d/%m/%Y"))
            x[1].append(float(at.loc[i, height/50 - 1]))
    elif rr > at.index[-1]:
        for i in range(1, at.index[-1], 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%d/%m/%Y"))
            x[1].append(float(at.loc[i, height/50 - 1]))
        a = parameters(x[1], season, int(itr), rr - at.index[-1])             # predict x and append values
        x[1] = a[4]
        for i in range(len(a[3])):                                            # appending the new dates
            last_date = x[0][-1]
            last_year = last_date.year
            last_month = last_date.month
            if last_month == 12:
                last_year += 1
                last_month = 0
            date = datetime(last_year, last_month + 1, 1)
            x[0].append(date)
    until_da = x[0][rr-2]
    data_value = x[1][rr-2]
    before_after = f"between 2020 and {until_da}"
    maximum = max(x[1])
    maximum_d = x[0][x[1].index(maximum)]
    return data_value, x[1], maximum, maximum_d, before_after, x[0]


def cell_atmo_info(height, yy, mm, xx):
    variable = data_sheets(height, yy, mm, xx, 144, 10)
    if xx == 'Density':
        zz = 'g/cm^3'
    if xx == 'Temperature':
        zz = 'kelvin'
    if xx == "Atomic Oxygen" or xx == "Atomic Nitrogen" or xx == "Argon" or xx == "Helium" or xx == "Hydrogen":
        zz = 'atom/cm^3'
    if xx == "Oxygen" or xx == "Nitrogen":
        zz = 'molecule/cm^3'
    flight_info = f"The {xx} at {yy}-{mm} = {variable[0]} {zz} \n" \
                  f"The Maximum {xx} {variable[4]} = {variable[2]} {zz} \n" \
                  f"occurrence in {variable[3]} \n" \
                  f"The Data per Month {variable[4]} = {variable[1]} \n" \
                  f" \n"
    return flight_info


def data_plot(height, yy, mm, xx, season_len, itr, out):
    prop = ["Argon", "Density", "Temperature", "Atomic Oxygen", "Oxygen", "Atomic Nitrogen", "Nitrogen", "Helium", "Hydrogen"]

    title = f"{height}km Height Plot"
    x = [[], []]                                                         # date / data
    at = pd.read_csv(resource_path(f'star_tk/data/{xx}.csv'), header = None)                    # reading the csv file data
    yy, mm = int(yy), int(mm)
    rr = (yy - 1996) * 12 + mm + 1                                       # find the row based on input date
    if rr < at.index[-1]:                                                # append data and date to list x
        for i in range(1, rr, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%d/%m/%Y"))
            x[1].append(float(at.loc[i, height/50 - 1]))
    elif rr > at.index[-1]:
        for i in range(1, at.index[-1], 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%d/%m/%Y"))
            x[1].append(float(at.loc[i, height/50 - 1]))
        a = parameters(x[1], season_len, int(itr), rr - at.index[-1])     # predict x and append values
        x[1] = a[4]
        for i in range(len(a[3])):                                        # appending the new dates
            last_date = x[0][-1]
            last_year = last_date.year
            last_month = last_date.month
            if last_month == 12:
                last_year += 1
                last_month = 0
            date = datetime(last_year, last_month + 1, 1)
            x[0].append(date)
    units = {"Density":"(g/cm^3)", "Temperature":"(keliven)", "Atomic Oxygen":"(atom/cm^3)", "Oxygen":"(particle/cm^3)",
                "Atomic Nitrogen":"(atom/cm^3)", "Nitrogen":"(particle/cm^3)", "Helium":"(atom/cm^3)", "Hydrogen":"(atom/cm^3)", 
                "Argon":"(particle/cm^3)"}
    fig = px.line(x, x=x[0], y=x[1], template="simple_white",labels={'y': f'{xx} {units[xx]}', 'x': 'Date'})
    fig.update_layout(title={'text': title, 'y': 0.96, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
                        font=dict(family="Courier New, monospace", size=11, color="black"))
    fig.update_traces(line_color='orange')
    fig.update_layout(dragmode='drawopenpath', newshape_line_color='cyan')
    fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=1, label="1m", step="month", stepmode="backward"), dict(count=6, label="6m", step="month", stepmode="backward"),
        dict(count=1, label="1y", step="year", stepmode="backward"), dict(step="all")])), rangeslider=dict(visible=True), type="date"))
    config = {'modeBarButtonsToAdd':['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape'],
                            'displaylogo': False, 'displayModeBar': True, "toImageButtonOptions": {"width": 1024, "height": 545}}
    if out == 'html':
        newfig = fig.to_html(include_plotlyjs='cdn', config=config)
        return newfig
    elif out == 'instant':
        fig.show(config=config)
    elif out == 'png':
        if not os.path.exists("images"):
            os.mkdir("images")
        fig.write_image("images/fig1.png")


# irradiance functions
# ----------------------------------------------------------------------------------------------------------------------


def irradiance(yy, mm, phi, season_len, itr):
    at = pd.read_csv(resource_path('star_tk/data/Irradiance.csv'), header = None)
    yy, mm = int(yy), int(mm)
    rr = (yy - 1976) * 12 + mm + 1
    x = [[], []]
    if rr < at.index[-1]:                                                # append data and date to list x
        for i in range(1, rr, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%d/%m/%Y"))
            x[1].append(float(at.loc[i, 1]))
        true_irr = x[1][-1]
        until_da = x[0][-1]
    elif rr > at.index[-1]:
        for i in range(1, at.index[-1], 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%d/%m/%Y"))
            x[1].append(float(at.loc[i, 1]))
        a = parameters(x[1], season_len, itr, rr - at.index[-1])         # predict x and append values
        x[1] = a[4]
        for i in range(len(a[3])):                                       # appending the new dates
            last_date = x[0][-1]
            last_year = last_date.year
            last_month = last_date.month
            if last_month == 12:
                last_year += 1
                last_month = 0
            date = datetime(last_year, last_month + 1, 1)
            x[0].append(date)
        true_irr = x[1][-1]
        until_da = x[0][-1]
    irr = true_irr * cos(float(phi) * (pi/180))
    if rr > at.index[-1]:
        before_after = f"since 2020 until {until_da}"
    else:
        before_after = f"since 1976 until {until_da}"
    angle = float(phi)
    counter = 0
    while angle > 90:
        angle = abs(angle - 90)
        counter += 1
    if counter % 2 == 0:
        direction = "Direct Orbit"
    else:
        direction = "Retrograde Orbit"
    maximum = max(x[1])
    dt = x[0][x[1].index(maximum)]
    return true_irr, irr, direction, dt, maximum, before_after


def irr_plot(yy, mm, season_len, itr):
    x = [[], []]
    at = pd.read_csv(resource_path('star_tk/data/Irradiance.csv'), header = None)
    yy, mm = int(yy), int(mm)
    rr = (yy - 1976)* 12 + mm + 1
    if rr < at.index[-1]:                                                 # append data and date to list x
        for i in range(1, rr, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%d/%m/%Y"))
            x[1].append(float(at.loc[i, 1]))
    elif rr > at.index[-1]:
        for i in range(1, at.index[-1], 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%d/%m/%Y"))
            x[1].append(float(at.loc[i, 1]))
        a = parameters(x[1], season_len, int(itr), rr - at.index[-1])     # predict x and append values
        x[1] = a[4]
        for i in range(len(a[3])):                                        # appending the new dates
            last_date = x[0][-1]
            last_year = last_date.year
            last_month = last_date.month
            if last_month == 12:
                last_year += 1
                last_month = 0
            date = datetime(last_year, last_month + 1, 1)
            x[0].append(date)
    fig = px.line(x, x=x[0], y=x[1], template="simple_white",labels={'y': f'Irradiance', 'x': 'Date'})
    fig.update_layout(title={'text':'Irradiance Plot', 'y': 0.96, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
                        font=dict(family="Courier New, monospace", size=11, color="black"))
    fig.update_traces(line_color='orange')
    fig.update_layout(dragmode='drawopenpath', newshape_line_color='cyan')
    fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=1, label="1m", step="month", stepmode="backward"), dict(count=6, label="6m", step="month", stepmode="backward"),
        dict(count=1, label="1y", step="year", stepmode="backward"), dict(step="all")])), rangeslider=dict(visible=True), type="date"))
    config = {'modeBarButtonsToAdd':['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape'],
                            'displaylogo': False, 'displayModeBar': True, "toImageButtonOptions": {"width": 1024, "height": 545}}
    fig.show(config=config)


def irr_plot1(yy, mm, phi, season_len, itr):
    x_ = [[], []]
    ir = irradiance(yy, mm, phi, season_len, itr)[0]
    print(phi)
    for i in range(-phi, phi, 1):
        z = ir * cos(float(i) * (pi/180))
        x_[0].append(z)
        x_[1].append(i)
    fig = px.line(x_, x=x_[1], y=x_[0], template="simple_white")
    fig.update_layout(title={'text': "Irradiance vs. Elevation", 'y': 1, 'x': 0.5},
                      xaxis_title="Elevation",
                      yaxis_title="Irradiance W/m^2",
                      font=dict(family="Courier New, monospace", size=18, color="black"))
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
    fig.update_traces(line_color='orange')
    fig.update_layout(dragmode='drawopenpath', newshape_line_color='cyan')
    config = {'modeBarButtonsToAdd':['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape'],
                            'displaylogo': False, 'displayModeBar': True, "toImageButtonOptions": {"width": 1024, "height": 545}}
    fig.show(config=config)


def cell_irr_info(yy, mm, phi, season_len, itr):
    var_able = irradiance(yy, mm, phi, season_len, itr)
    total_irr = var_able[0]
    max_irr = var_able[0]
    min_irr = var_able[1]
    orbit_type = var_able[2]
    max_dat = var_able[3]
    max_irr_bg = var_able[4]
    before_aft = var_able[5]
    flight_info = f"Total Solar Irradiance = {total_irr} W/m^2 \n" \
                  f"Maximum Solar Irradiance at latitude 0 degree = {max_irr} W/m^2 \n" \
                  f"Minimum solar Irradiance at latitude {phi} degree = {min_irr} W/m^2 \n" \
                  f"Orbit Type = {orbit_type} \n" \
                  f"The Maximum Irradiance {before_aft} is = {max_irr_bg} W/m^2 \n" \
                  f"occurrence in {max_dat}"
    return flight_info


# drag functions
# ----------------------------------------------------------------------------------------------------------------------


def a_oblateness(simajor, argp, incli, true, eccen):
    m_u = 3.986004418 * (10 ** 5)    # km3/s2
    j_2 = 1.08262668 * (10 ** -3)
    R_e = 6371
    s_a = simajor
    ecc = eccen
    tru = true
    r_s = (s_a * (1 - (ecc ** 2)))/(1 + ecc * cos(tru))
    agp = argp
    inc = incli
    u_s = agp + tru
    m_m = sqrt(m_u/(s_a ** 3))
    dt = []
    for i in range(10 ** 30):
        true += 1
        da_1 = (3 * m_u * j_2 * (R_e ** 2))/(r_s ** 4)
        da_2 = ((ecc * sin(tru))/(m_m * sqrt(1 - (ecc ** 2)))) * (3 * (sin(inc) ** 2) * (sin(u_s) ** 2) - 1)
        da_3 = ((2 * s_a * sqrt(1 - (ecc ** 2)))/(m_m * r_s)) * ((sin(inc) ** 2) * sin(u_s) * cos(u_s))
        da = da_1 * (da_2 - da_3)
        s_a = s_a - abs(da)
        if s_a <= 100:
            dt.append(i)
            break
        if s_a >= 50000:
            dt.append(i)
            break
    return da, max(dt), s_a


def e_oblateness(simajor, argp, incli, true, eccen):
    m_u = 3.986004418 * (10 ** 5)    # km3/s2
    j_2 = 1.08262668 * (10 ** -3)
    R_e = 6371
    s_a = simajor
    ecc = eccen
    tru = true
    r_s = (s_a * (1 - (ecc ** 2)))/(1 + ecc * cos(tru))
    agp = argp
    inc = incli
    u_s = agp + tru
    m_m = sqrt(m_u/(s_a ** 3))
    dt = []
    for i in range(10 ** 30):
        true += 1
        de_1 = ((3 * m_u * j_2 * R_e ** 2)/(r_s ** 4)) * (sqrt(1 - ecc ** 2)/(m_m * s_a))
        de_2 = 3/2 * sin(tru) * (sin(inc) ** 2) * (sin(u_s) ** 2) - 1/2 * sin(tru)
        de_3 = (sin(inc) ** 2) * sin(u_s) * cos(u_s) * cos(tru)
        de_4 = ((ecc + cos(tru))/(1 + ecc * cos(tru))) * ((sin(inc) ** 2) * sin(u_s) * cos(u_s))
        de = de_1 * (de_2 - de_3 - de_4)
        ecc = ecc - abs(de)
        if de <= 0:
            dt.append(i)
            break
    return de, max(dt)


def search(s_a, yy, mm):
    x = [1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100]
    for i in range(0, len(x)):
        if x[i] > s_a > x[i + 1]:
            a = ((s_a - x[i + 1])/50)
            b = data_sheets(x[i], yy, mm, 'Density', 144, 10)[0]
            c = data_sheets(x[i + 1], yy, mm, 'Density', 144, 10)[0]
            d = a * (c - b) + b
        if x[i] == s_a:
            d = data_sheets(x[i], yy, mm, 'Density', 144, 10)[0]
    if s_a >= 1000:
        b = data_sheets(1000, yy, mm, 'Density', 144, 10)[0]
    return d


def a_drag(simajor, ecc, true, area0, mass, yy, mm):
    s_a = simajor
    tru = true
    m_u = 3.986004418 * (10 ** 5)    # km3/s2
    m_m = sqrt(m_u/(s_a ** 3))
    A = area0
    m = mass
    d = search(simajor, yy, mm)
    ecc = ecc
    v = sqrt(m_u * ((1 + ecc * cos(tru))/(s_a * (1 - (ecc ** 2)))))

    a_dens = -(A/m) * (0.027 * d * v ** 2) / (m_m * sqrt(1 - ecc ** 2)) * sqrt((1 + ecc ** 2 + 2 * ecc * cos(tru)))
    s_a = s_a / abs(a_dens)
    return a_dens, s_a


def e_drag(simajor, ecc, true, area0, mass, yy, mm):
    s_a = simajor
    tru = true
    m_u = 3.986004418 * (10 ** 5)  # km3/s2
    m_m = sqrt(m_u / (s_a ** 3))
    A = area0
    m = mass
    d = search(simajor, yy, mm)
    ecc = ecc
    v = sqrt(m_u * ((1 + ecc * cos(tru))/(s_a * (1 - (ecc ** 2)))))

    e_dens_1_1 = -(A/m) * (0.027 * d * v ** 2)
    e_dens_1_2 = sqrt(1 - (ecc ** 2)) * (cos(tru) + ecc)
    e_dens_1 = e_dens_1_1 * e_dens_1_2
    e_dens_2 = m_m * s_a * sqrt(1 + (ecc ** 2) + 2 * ecc * cos(tru))
    e_dens = (e_dens_1 / e_dens_2)
    ecc = ecc/abs(e_dens)
    return e_dens, ecc


# CME functions
# ---------------------------------------------------------------------------------------------------------------------


def julian(year, month, day):
    ''' julian date function '''
    if month < 2 :
        year = year - 1
        month = month + 12
    if year > 1582 :
        a = int(year/100)
        b = 2 - a + int(a/4)
    elif month <= 10:
        if day <= 15:
            b = 0
        else:
            a = int(year/100)
            b = 2 - a + int(a/4)
    if year < 0 :
        c = int((365.25 * year) - 0.75)
    else : c = int(365.25 * year)
    d = int(30.6001 * (month + 1))
    j_date =  b + c + d + day + 1720994.5
    return j_date


def cme_sheets(yy, mm, dd, xx, season, itr):
    r'''
    this function search in data and returns desired data at the input date, the data list, the max and max date and pefore or after forecast
    inputs year 1996 - 2030, month, day, property ["Central PA","Mass","width","Linear Speed"]
    '''
    prop = {'Central PA':1, 'Linear Speed':2, 'MPA':3, '20R Speed':4, 'Width':5, 'SSN':6}
    yy, mm, dd = int(yy), int(mm), int(dd)
    cme_time = int(julian(yy, mm, dd) - julian(1996, 1, 11) + 4)
    at = pd.read_csv(resource_path('star_tk/data/CME_2030.csv'), header = None)
    x = [[], []]
    if cme_time < at.index[-1]:                                                     # append data and date to list x
        for i in range(1, cme_time, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%m/%d/%Y"))
            x[1].append(float(at.loc[i, prop[xx]]))
    elif cme_time > at.index[-1]:
        for i in range(1, at.index[-1], 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%m/%d/%Y"))
            x[1].append(float(at.loc[i, prop[xx]]))
        a = parameters(x[1], season, int(itr), cme_time - at.index[-1])             # predict x and append values
        x[1] = a[4]
        for i in range(len(a[3])):                                                  # appending the new dates
            date = x[0][-1]
            date += timedelta(days=1)
            x[0].append(date)
    until_da = x[0][cme_time-2]
    data_value = x[1][cme_time-2]
    before_after = f"between 1996 and {until_da}"
    maximum = max(x[1])
    maximum_d = x[0][x[1].index(maximum)]
    return data_value, x[1], maximum, maximum_d, before_after, x[0]


def cell_cme_info(yy, mm, dd, xx, season=4383, itr=10):
    variable = cme_sheets(yy, mm, dd, xx, season, itr)
    zz = {'Central PA' : 'degree', 'Linear Speed' : 'Km/s', 'Width' : 'degree', '20R Speed' : 'Km/s', 'MPA':'degree', 'SSN':'Spots'}
    flight_info = f"The {xx} at {yy}-{mm}-{dd} = {variable[0]} {zz[xx]} \n" \
                f"The Maximum {xx} {variable[4]} = {variable[2]} {zz[xx]} \n" \
                f"occurrence in {variable[3]} \n" \
                f"The Data per day {variable[4]} = {variable[1]} \n" \
                  f" \n"
    return flight_info


def cme_plot(yy, mm, dd, xx, season, itr, out):
    r'''
    this function search in data and returns desired data at the input date, the data list, the max and max date and pefore or after forecast
    inputs year 1996 - 2030, month, day, property ["Central PA","Mass","width","Linear Speed"]
    '''
    prop = {'Central PA':1, 'Linear Speed':2, 'MPA':3, '20R Speed':4, 'Width':5, 'SSN':6}
    title = f"{xx}"
    yy, mm, dd = int(yy), int(mm), int(dd)
    cme_time = int(julian(yy, mm, dd) - julian(1996, 1, 10) + 4)
    at = pd.read_csv(resource_path('star_tk/data/CME_2030.csv'), header = None)
    x = [[], []]
    if cme_time < at.index[-1]:                                                     # append data and date to list x
        for i in range(1, cme_time, 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%m/%d/%Y"))
            x[1].append(float(at.loc[i, prop[xx]]))
    elif cme_time > at.index[-1]:
        for i in range(1, at.index[-1], 1):
            x[0].append(datetime.strptime(at.loc[i, 0], "%m/%d/%Y"))
            x[1].append(float(at.loc[i, prop[xx]]))
        a = parameters(x[1], season, int(itr), cme_time - at.index[-1])             # predict x and append values
        x[1] = a[4]
        for i in range(len(a[3])):                                                  # appending the new dates
            date = x[0][-1]
            date += timedelta(days=1)
            x[0].append(date)
    units = {'Central PA' : 'degree', 'Linear Speed' : 'Km/s', 'Width' : 'degree', '20R Speed' : 'Km/s', 'MPA':'degree', 'SSN':'Spot'}
    fig = px.line(x, x=x[0], y=x[1], template="simple_white",labels={'y': f'{xx} {units[xx]}', 'x': 'Date'})
    fig.update_layout(title={'text': title, 'y': 0.06, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'bottom'},
                        font=dict(family="Courier New, monospace", size=11, color="black"))
    fig.update_traces(line_color='orange')
    fig.update_layout(dragmode='drawopenpath', newshape_line_color='cyan')
    fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=1, label="1m", step="month", stepmode="backward"), dict(count=6, label="6m", step="month", stepmode="backward"),
        dict(count=1, label="1y", step="year", stepmode="backward"), dict(step="all")])), rangeslider=dict(visible=True), type="date"))
    config = {'modeBarButtonsToAdd':['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape'],
                            'displaylogo': False, 'displayModeBar': True, "toImageButtonOptions": {"width": 1024, "height": 545}}
    if out == 'html':
        newfig = fig.to_html(include_plotlyjs='cdn', config=config)
        return newfig
    elif out == 'instant':
        fig.show(config=config)
    elif out == 'png':
        if not os.path.exists("images"):
            os.mkdir("images")
        fig.write_image("images/fig1.png")


# debries functions
# ----------------------------------------------------------------------------------------------------------------------


def deb_plot(rP, rA, Wo, TAo, wpo, incl, n_periods, curve_d, out):
    '''
    ploting debris objects against the main object
    inputs, Pregree position vector, apogee position vector, right ascention of node, true anomaly,
    argument of pregee, Inclination, desired periods, resolution points
    '''
    xx, yy, zz = [], [], []             # right ascentions, declinations, and debris names
    at = pd.read_csv(resource_path('star_tk/data/Debris.csv'), header = None)
    a = (rA + rP)/2
    for i in range(1, at.index[-1]):
        # debri semi major axis
        x = float(at.loc[i, 18])
        a = a
        if x >= a-5:
            if x <= a+5:
                # Ground track inputs rPD, rAD, inclx, raanx, argpx, nux
                rPD = float(at.loc[i, 21]) + 6378
                rAD = float(at.loc[i, 20]) + 6378
                inclx = float(at.loc[i, 6])
                raanx = float(at.loc[i, 7])
                argpx = float(at.loc[i, 8])
                nux = TAo
                lable = f'{at.loc[i, 1]}' + f'{at.loc[i, 2]}'
                # ground track raan, decli lists
                debri = Orbit().groundtrack(rPD, rAD, raanx, nux, argpx, inclx, n_periods, curve_d)
                xx.append(debri[0])     # append debri raanx
                yy.append(debri[1])     # append debri decli
                zz.append(lable)        # append debri name_ID
    # ground track the main object
    satellite = Orbit().groundtrack(rP, rA, Wo, TAo, wpo, incl, n_periods, curve_d)
    xx.append(satellite[0])             # append satellite raanx
    yy.append(satellite[1])             # append satellite decli
    zz.append('Satellite')              # append satellite name
    # plotinf the main object using line_geo
    track = px.line_geo(lat=yy[-1], lon=xx[-1])
    # track.update_layout(title={'text': 'Ground Track', 'y': 0.99, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
    #                font=dict(family="Courier New, monospace", size=18, color="black"))
    # looping debris tracks and debris objects
    for i in range(len(xx)-1):
        track.add_trace(go.Scattergeo(lat=yy[i], lon=xx[i], line=dict(dash='solid'), name=f"{zz[i]}", text=f"{zz[i]}"))
        track.add_trace(go.Scattergeo(lat=[yy[i][-1]], lon=[xx[i][-1]], mode='markers', name=f"{zz[i]}",
                        marker={"size": 10, "symbol": "circle", "color":'rgb(162,228,184)',
                        'line':dict(color='gray', width=2)}, showlegend=False))
    # adding debris tracks
    track.add_trace(go.Scattergeo(lat=[yy[-1][-1]], lon=[xx[-1][-1]], mode='markers', name=f"{zz[i]}",
                    marker={"size": 10, "symbol": "circle", "color":'rgb(162,228,184)',
                    'line':dict(color='gray', width=2)}, showlegend=False))
    # ploting shape, flat or 3D
    track.update_geos(projection=dict(type="orthographic", rotation_lon=100))
    config = {'modeBarButtonsToAdd':['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape'],
                            'displaylogo': False, 'displayModeBar': True, "toImageButtonOptions": {"width": 1024, "height": 545}}
    if out == 'html':
        newfig = track.to_html(include_plotlyjs='cdn', config=config)
        return newfig
    elif out == 'instant':
        track.show(config=config)
    elif out == 'png':
        if not os.path.exists("images"):
            os.mkdir("images")
            track.write_image("images/fig1.png")


def deb_info(rP, rA):
    '''
    extract debris objects informations from data file
    inputs, Pregree position vector, apge position
    '''
    a = (rA + rP)/2                   # debri semi major axis
    # appending lists of satellite data from data sheet
    aa, na, sz, pe, mm = [], [], [], [], []
    apo, pre, ecc, inc = [], [], [], []
    at = pd.read_csv(resource_path('star_tk/data/Debris.csv'), header = None)
    for i in range(2, at.index[-1]):
        x = int(float(at.loc[i, 18]))
        if x >= a-5:
            if x <= a+5:
                aa.append(x)
                lable = f'{at.loc[i, 1]}' + f'{at.loc[i, 2]}'
                na.append(lable)
                size = at.loc[i, 23]
                sz.append(size)
                period = float(at.loc[i, 19])
                pe.append(period)
                Apogee = float(at.loc[i, 20]) + 6378
                apo.append(Apogee)
                Pregee = float(at.loc[i, 21]) + 6378
                pre.append(Pregee)
                Eccentricity = float(at.loc[i, 5])
                ecc.append(Eccentricity)
                Inclination = float(at.loc[i, 6])
                inc.append(Inclination)
                Mean_Motion = float(at.loc[i, 4])
                mm.append(Mean_Motion)
    # information in formated text
    length = len(aa)
    information = f'There is {len(aa)} debris in a collision range with the satellite'
    info = []
    for i in range(length):
        information2 = f'\n The {na[i]} \n' \
                    f'             Size = {sz[i]} \n' \
                    f'             Semi-major axis = {aa[i]} km \n' \
                    f'             Period = {pe[i]} minutes \n' \
                    f'             Apogee = {apo[i]} km \n' \
                    f'             Pregree = {pre[i]} km \n' \
                    f'             Inclination = {inc[i]} degree \n' \
                    f'             Eccentricity = {ecc[i]} \n' \
                    f'             Mean Motion = {mm[i]} \n'
        info.append(information2)
    return information, info


# visiualization functions
# ----------------------------------------------------------------------------------------------------------------------


def orb_calc(rP, rA, Wo, TAo, wpo, incl, n_periods, curve_d, out):
    y = Orbit()
    x = y.groundtrack(rP, rA, Wo, TAo, wpo, incl, n_periods, curve_d)
    right = x[0]
    decle = x[1]
    track = px.line_geo(lat=decle, lon=right)
    # track.update_layout(title={'text': 'Ground Track', 'y': 0.99, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
    #                 font=dict(family="Courier New, monospace", size=18, color="black"))
    track.update_layout(colorway = ['rgb(0, 0, 0)'], margin={"r":0,"t":0,"l":0,"b":0})
    # margin={"r":0,"t":0,"l":0,"b":0}, geo = dict(resolution=50, lataxis_showgrid=True, lonaxis_showgrid=True,
    # showcountries = True, landcolor = 'rgb(230, 145, 56)', oceancolor = 'rgb(0, 255, 255))')
    track.add_trace(go.Scattergeo(lat=[decle[-1]], lon=[right[-1]], mode='markers', name='satellite',
                    marker={"size": 10, "symbol": "circle", "color":'rgb(162,228,184)',
                    'line':dict(color='gray', width=2)}, showlegend=False))
    config = {'modeBarButtonsToAdd':['drawline', 'drawopenpath', 'drawclosedpath', 'drawcircle', 'drawrect', 'eraseshape'],
                            'displaylogo': False, 'displayModeBar': True, "toImageButtonOptions": {"width": 1024, "height": 545}}
    if out == 'html':
        newfig = track.to_html(include_plotlyjs='cdn', config=config)
        return newfig
    elif out == 'instant':
        track.show(config=config)
    elif out == 'png':
        if not os.path.exists("images"):
            os.mkdir("images")
            track.write_image("images/fig1.png")


def orb_info_ri(h, sa, ecc, inc, raan, argp, nu):
    '''
    coe return [a, h, H, e, E, period, energy, mean_n, degree(incl), degrees(RA), degrees(w), degrees(TA)]
    returns semi_major axis, h vector, h magnetude, eccentricity vector, eccentricity magnetude, period, energy, mean motion,
    inclination, right ascention, argument of pregee, true anomaly
    '''
    mu = 398600
    R, V = Orbit().sv_from_coe(h, ecc, raan, inc, argp, nu)
    obj = Orbit().coe_from_sv(R, V, mu)
    angle = float(obj[8])
    counter = 0
    direction = None
    while angle > 90:
        angle = abs(angle - 90)
        counter += 1
    if counter % 2 == 0:
        direction = "Direct Orbit"
    else:
        direction = "Retrograde Orbit"
    rr = R
    vv = V
    s_a, h_m, h_v, e_m, e_v, p_e = obj[0], obj[1], obj[2], obj[3], obj[4], obj[5]
    e_n, m_n, i_n, r_a, a_p, t_a = obj[6], obj[7], obj[8], obj[9], obj[10], obj[11]
    variable = [direction, rr, vv, s_a, h_m, h_v, e_m, e_v, p_e, e_n, m_n, i_n, r_a, a_p, t_a]
    s_inf = f"The orbit kind = {variable[0]} \n" \
            f"The orbit r vector = {variable[1]} Km\n" \
            f"The orbit v vector = {variable[2]} Km/s\n" \
            f"The orbit semi_major axis = {variable[3]} Km\n" \
            f"The orbit h magnetude = {variable[4]} Km^2/s\n" \
            f"The orbit h vector = {variable[5]} Km^2/s\n" \
            f"The orbit e magnetude = {variable[6]} \n" \
            f"The orbit e vector = {variable[7]} \n" \
            f"The orbit period = {variable[8]} s\n" \
            f"The orbit energy = {variable[9]} Kg . Km^2/s^2\n" \
            f"The orbit mean motion = {variable[10]} orbit/s\n" \
            f"The orbit inclination = {variable[11]} degree\n" \
            f"The orbit right ascention = {variable[12]} degree\n" \
            f"The orbit argument of pregee = {variable[13]} degree\n" \
            f"The orbital true anomaly = {variable[14]} degree\n" \
            f" \n"
    return s_inf

