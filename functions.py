import pandas as pd
import plotly.express as px
import math, sys, os
from datetime import datetime
from smoothing import *

# main functions
# ----------------------------------------------------------------------------------------------------------------------


def data_sheets(height, checkbox, yy, mm, xx, season, itr):
    prop = ["Argon", "Density", "Temperature", "Atomic Oxygen", "Oxygen", "Atomic Nitrogen", "Nitogen", "Helium", "Hydrogen"]
    at = pd.read_csv(f'data/{xx}.csv', header = None)
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


def cell_atmo_info(height, checkbox, yy, mm, xx):
    variable = data_sheets(height, checkbox, yy, mm, xx, 144, 10)
    if xx == 'Density':
        zz = 'g/cm^3'
    if xx == 'Temperature':
        zz = 'kelvin'
    if xx == "Atomic Oxygen" or xx == "Atomic Nitrogen" or xx == "Argon" or xx == "Helium" or xx == "Hydrogen":
        zz = 'atom/cm^3'
    if xx == "Oxygen" or xx == "Nitogen":
        zz = 'molecule/cm^3'
    flight_info = f"The {xx} at {yy}-{mm} = {variable[0]} {zz} \n" \
                  f"The Maximum {xx} {variable[4]} = {variable[2]} {zz} \n" \
                  f"occurrence in {variable[3]} \n" \
                  f"The Data per Month {variable[4]} = {variable[1]} \n" \
                  f" \n"
    return flight_info


def data_plot(height, checkbox, yy, mm, xx, season_len, itr, out):
    prop = ["Argon", "Density", "Temperature", "Atomic Oxygen", "Oxygen", "Atomic Nitrogen", "Nitogen", "Helium", "Hydrogen"]

    title = f"{height}km Height Plot"
    x = [[], []]                                                         # date / data
    at = pd.read_csv(f'data/{xx}.csv', header = None)                    # reading the csv file data
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
                "Atomic Nitrogen":"(atom/cm^3)", "Nitogen":"(particle/cm^3)", "Helium":"(atom/cm^3)", "Hydrogen":"(atom/cm^3)"}
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


def irradiance(yy, mm, phi):
    at = pd.read_csv(f'data/Irradiance.csv', header = None)
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
        a = parameters(x[1], 144, int(10), rr - at.index[-1])     # predict x and append values
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
        true_irr = x[1][-1]
        until_da = x[0][-1]
    irr = true_irr * cos(float(phi) * (pi/180))
    if rr > at.index[-1]:
        before_after = f"since 2020 until {until_da}"
    else:
        before_after = f"since 1996 until {until_da}"
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
    at = pd.read_csv(f'data/Irradiance.csv', header = None)
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


def irr_plot1(yy, mm, phi):
    x = [[], []]
    for i in range(-phi, phi, 1):
        ir = irradiance(yy, mm, i)[1]
        x[0].append(ir)
        x[1].append(i)
    fig = px.line(x, x=x[1], y=x[0], template="simple_white")
    fig.update_layout(title={'text': "Irradiance vs. Elevation", 'y': 1, 'x': 0.5},
                      xaxis_title="Elevation",
                      yaxis_title="Irradiance W/m^2",
                      font=dict(family="Courier New, monospace", size=18, color="black"))
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
    fig.show()


def cell_irr_info(yy, mm, phi):
    total_irr = irradiance(yy, mm, phi)[0]
    max_irr = irradiance(yy, mm, phi)[0]
    min_irr = irradiance(yy, mm, phi)[1]
    orbit_type = irradiance(yy, mm, phi)[2]
    max_pg_dat = irradiance(yy, mm, phi)[3]
    max_irr_bg = irradiance(yy, mm, phi)[4]
    before_aft = irradiance(yy, mm, phi)[5]
    flight_info = f"Total Solar Irradiance = {total_irr} W/m^2 \n" \
                  f"Maximum Solar Irradiance at latitude 0 degree = {max_irr} W/m^2 \n" \
                  f"Minimum solar Irradiance at latitude {phi} degree = {min_irr} W/m^2 \n" \
                  f"Orbit Type = {orbit_type} \n" \
                  f"The Maximum Irradiance {before_aft} is = {max_irr_bg} W/m^2 \n" \
                  f"occurrence in {max_pg_dat}"
    return flight_info

    print(x)
# ----------------------------------------------------------------------------------------------------------------------
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
            b = data_sheets(x[i], 1, yy, mm, 'density')[0]
            c = data_sheets(x[i + 1], 1, yy, mm, 'density')[0]
            d = a * (c - b) + b
        if x[i] == s_a:
            d = data_sheets(x[i], 1, yy, mm, 'density')[0]
    if s_a >= 1000:
        b = data_sheets(1000, 1, yy, mm, 'density')[0]
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


# ----------------------------------------------------------------------------------------------------------------------
# CME functions
# ----------------------------------------------------------------------------------------------------------------------


def cme_sheets(checkbox, yy, mm, dd, xx):
    yy, mm, dd = int(yy), int(mm), int(dd)
    rr0 = dateutil.parser.parse(f'{yy}.{mm}.{dd}')
    rr1 = dateutil.parser.parse('1996.1.10')
    cme_time = int(astropy.time.Time(rr0).jd - astropy.time.Time(rr1).jd) + 1
    if checkbox:
        at = xl.load_workbook('data/CME_forecast_2030.xlsx')
    xx = str(xx)
    sheet = at[xx]
    cell0 = sheet.cell(cme_time, 2)
    cell1 = sheet.cell(cme_time, 1)
    until_da = cell1.value
    data_value = cell0.value
    before_after = f"from 1996-01-11 to {until_da}"
    x = []
    if cme_time > 8758:
        st = 8758
    else:
        st = 2
    for row in sheet[f'B{st}':f'B{cme_time}']:
        for cell in row:
            y = cell.value
            x.append(y)
    maximum = max(x)
    for row in sheet[f'B{st}':f'B{cme_time}']:
        for cell in row:
            if cell.value == maximum:
                dt = sheet.cell(row=cell.row, column=1).value
    return data_value, cme_time, x, maximum, dt, before_after


def cell_cme_info(checkbox, yy, mm, dd, xx):
    variable = cme_sheets(checkbox, yy, mm, dd, xx)
    if xx == 'Central PA' or xx == 'width':
        zz = 'degree'
    if xx == 'Linear speed':
        zz = 'Km/s'
    if xx == 'Mass':
        zz = 'gram'
    flight_info = f"The {xx} at {yy}-{mm}-{dd} = {variable[0]} {zz} \n" \
                  f"The Maximum {xx} {variable[5]} = {variable[3]} {zz} \n" \
                  f"occurrence in {variable[4]} \n" \
                  f"The Data Der day {variable[5]} = {variable[2]} \n" \
                  f" \n"
    return flight_info


def cme_plot(yy, mm, dd, xx):
    # xx is the column number 2-central PA 3-linear speed 6-width
    at = 'data/CME_forecast_2030.xlsx'
    book = xl.load_workbook(at)
    sheet = book['central PA']
    cell = str(sheet.cell(1, xx).value)
    yy, mm, dd = int(yy), int(mm), int(dd)
    rr0 = dateutil.parser.parse(f'{yy}.{mm}.{dd}')
    rr1 = dateutil.parser.parse('1996.1.10')
    rr2 = int(astropy.time.Time(rr0).jd - astropy.time.Time(rr1).jd) + 1
    df = pd.read_excel(at, sheet_name='central PA', nrows=rr2)
    fig = px.line(df, x='Date', y=cell, template="simple_white")  # text='Central PA'
    fig.update_layout(title={'text': "CME Forecast", 'y': 0.9, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
                      font=dict(family="Courier New, monospace", size=18, color="black"))
    fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
        dict(count=1,
             label="1m",
             step="month",
             stepmode="backward"),
        dict(count=6,
             label="6m",
             step="month",
             stepmode="backward"),
        dict(count=1,
             label="1y",
             step="year",
             stepmode="backward"),
        dict(step="all")])), rangeslider=dict(visible=True), type="date"))
    fig.show()


# ----------------------------------------------------------------------------------------------------------------------
# debries functions
# ----------------------------------------------------------------------------------------------------------------------


def find(element, matrix):
    for i in range(len(matrix)):
        if matrix[i] == element:
            return i


def deb_plot(a, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss):
    y = []
    z = []
    at = xl.load_workbook('data/Debris.xlsx')
    sheet = at['celestrak.com']
    rows = range(2, 4036)
    for i in rows:
        x = sheet.cell(i, column=8).value
        a = a
        if x >= a-5:
            if x <= a+5:
                ax = x * units.km
                eccx = sheet.cell(i, column=9).value * units.dimensionless_unscaled
                incx = sheet.cell(i, column=5).value * units.deg
                raanx = 0 * units.deg
                argpx = 0 * units.deg
                nux = 0 * units.deg
                tx = time.Time(f'{yy}-{mm}-{dd} {hh}:{mn}:{ss}')
                orbx = Orbit.from_classical(Earth, ax, eccx, incx, raanx, argpx, nux, tx)
                AA1 = 1 * units.m ** 2
                C_Dx = 0.027
                m1 = 1 * units.kg
                spcx = spacecraft.Spacecraft(AA1, C_Dx, m1)
                satellitex = EarthSatellite(orbx, spcx)
                y.append(satellitex)
                lable = f'{sheet.cell(i, column=3).value}' + f'{sheet.cell(i, column=2).value}'
                z.append(lable)
    a = a * units.km
    ecc = ecc * units.dimensionless_unscaled
    inc = inc * units.deg
    raan = raan * units.deg
    argp = argp * units.deg
    nu = nu * units.deg
    t = time.Time(f'{yy}-{mm}-{dd} {hh}:{mn}:{ss}')
    orb = Orbit.from_classical(Earth, a, ecc, inc, raan, argp, nu, t)
    AA = 1 * units.m ** 2
    C_D = 0.027
    m = 10 * units.kg
    spc = spacecraft.Spacecraft(AA, C_D, m)
    satellite = EarthSatellite(orb, spc)
    y.append(satellite)
    z.append('Satellite')
    t_span = time_range(orb.epoch, periods=300, end=orb.epoch + orb.period)
    track = GroundtrackPlotter()
    track.update_layout(title=dict(text='Satellite path'))
    for satellites in y:
        track.plot(satellites, t_span, label=f"{z[find(satellites, y)]}", color="black",
                   marker={"size": 10, "symbol": "circle", "line": {"width": 1, "color": "white"}})
        track.update_geos(projection=dict(type="orthographic"))
    track.fig.show()


def deb_info(a):
    aa = []
    na = []
    pe = []
    inc = []
    apo = []
    pre = []
    ecc = []
    at = xl.load_workbook('data/Debris.xlsx')
    sheet = at['celestrak.com']
    rows = range(2, 4036)
    for i in rows:
        x = sheet.cell(i, column=8).value
        a = a
        if x >= a-5:
            if x <= a+5:
                aa.append(x)
                lable = f'{sheet.cell(i, column=3).value}' + f' {sheet.cell(i, column=2).value}'
                na.append(lable)
                period = sheet.cell(i, column=4)
                pe.append(period)
                Inclination = sheet.cell(i, column=5).value
                inc.append(Inclination)
                Apogee = sheet.cell(i, column=6).value
                apo.append(Apogee)
                Pregee = sheet.cell(i, column=7).value
                pre.append(Pregee)
                Eccentricity = sheet.cell(i, column=9).value
                ecc.append(Eccentricity)
    length = len(aa)
    information = f'There is {len(aa)} debris in a collision range with the satellite'
    info = []
    for i in range(length):
        information2 = f'\n The {na[i]} \n' \
                       f'             Semi-major axis = {aa[i]} km \n' \
                       f'             Inclination = {inc[i]} degree \n' \
                       f'             Period = {pe[i]} minutes \n' \
                       f'             Apogee = {apo[i]} km \n' \
                       f'             Pregree = {pre[i]} km \n' \
                       f'             Eccentricity = {ecc[i]} \n'
        info.append(information2)
    return information, info


# ----------------------------------------------------------------------------------------------------------------------
# visiualization functions
# ----------------------------------------------------------------------------------------------------------------------


def orb_calc(sa, ecc, inc, raan, argp, nu, yy, mm, hh, mn, ss, dd, p, aa, m):
    a1 = sa * units.km
    ecc1 = ecc * units.dimensionless_unscaled
    inc1 = inc * units.deg
    raan1 = raan * units.deg
    argp1 = argp * units.deg
    nu1 = nu * units.deg
    t1 = time.Time(f'{yy}-{mm}-{dd} {hh}:{mn}:{ss}')
    orb = Orbit.from_classical(Earth, a1, ecc1, inc1, raan1, argp1, nu1, t1)
    period = p * orb.period
    AA1 = aa * units.m ** 2
    C_D = 0.027
    m1 = m * units.kg
    spc = spacecraft.Spacecraft(AA1, C_D, m1)
    satellite = EarthSatellite(orb, spc)
    t_span = time_range(orb.epoch, periods=300, end=orb.epoch + period)
    track = GroundtrackPlotter()
    track.update_layout(title=dict(text='Satellite path'))
    track.plot(satellite, t_span, label="Sat", color="black",
               marker={"size": 10, "symbol": "circle", "line": {"width": 1, "color": "white"}})
    # track.update_geos(projection=dict(type="orthographic", rotation_lon=100))
    track.fig.show()


def orb_info(sa, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss):
    a1 = sa * units.km
    ecc1 = ecc * units.dimensionless_unscaled
    inc1 = inc * units.deg
    raan1 = raan * units.deg
    argp1 = argp * units.deg
    nu1 = nu * units.deg
    t1 = time.Time(f'{yy}-{mm}-{dd} {hh}:{mn}:{ss}')
    orb = Orbit.from_classical(Earth, a1, ecc1, inc1, raan1, argp1, nu1, t1)
    angle = float(ecc)
    counter = 0
    while angle > 90:
        angle = abs(angle - 90)
        counter += 1
    if counter % 2 == 0:
        direction = "Direct Orbit"
    else:
        direction = "Retrograde Orbit"
    rr = orb.r
    vv = orb.v
    ee = orb.e_vec
    hv = orb.h_vec
    hh = orb.h_mag
    en = orb.energy
    ap = orb.r_a
    pe = orb.r_p
    mn = orb.n
    return direction, rr, vv, ee, hv, hh, en, ap, pe, mn, orb.period


def orb_info_ri(sa, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss):
    variable = orb_info(sa, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss)
    flight_info = f"The orbit kind = {variable[0]} \n" \
                  f"The orbit r vector = {variable[1]} \n" \
                  f"The orbit v vector = {variable[2]} \n" \
                  f"The orbit e vector = {variable[3]} \n" \
                  f"The orbit h vector = {variable[4]} \n" \
                  f"The orbit h magnetude = {variable[5]} \n" \
                  f"The orbit energy = {variable[6]} \n" \
                  f"The orbit apogee = {variable[7]} \n" \
                  f"The orbit pregee = {variable[8]} \n" \
                  f"The orbit mean motion = {variable[9]} \n" \
                  f"The orbital period = {variable[10]} \n" \
                  f" \n"
    return flight_info

