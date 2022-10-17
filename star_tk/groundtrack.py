from math import *


'''
mu              - gravitational parameter (km^3/s^2)
deg             - factor that converts degrees to radians
J2              - second zonal harmonic
Re              - earth’s radius (km)
we              - earth’s angular velocity (rad/s)
rP              - perigee of orbit (km)
rA              - apogee of orbit (km)
TA,TAo          - true anomaly, initial true anomaly of satellite (rad)
RA, RAo	        - right ascension, initial right ascension of the node (rad)
incl	        - orbit inclination (rad)
wp, wpo	        - argument of perigee, initial argument of perigee (rad)
Wo	            - Right ascensions of ascending node(rad)
n_periodsa	    - number of periods for which ground track is to be plotted
a	            - semimajor axis of orbit (km)
T	            - period of orbit (s)
e	            - eccentricity of orbit
h	            - angular momentum of orbit (km^2/s)
E, Eo	        - eccentric anomaly, initial eccentric anomaly (rad)
M, Mo	        - mean anomaly, initial mean anomaly (rad)
to, tf	        - initial and final times for the ground track (s)
fac	            - common factor in Equations 4.53 and 4.53
RAdot	        - rate of regression of the node (rad/s)
wpdot	        - rate of advance of perigee (rad/s)
times	        - times at which ground track is plotted (s)
ra	            - vector of right ascensions of the spacecraft (deg)
dec	            - vector of declinations of the spacecraft (deg)
TA	            - true anomaly (rad)
r	            - perifocal position vector of satellite (km)
R	            - geocentric equatorial position vector (km)
R1	            - DCM for rotation about z through RA
R2	            - DCM for rotation about x through incl
R3	            - DCM for rotation about z through wp
QxX	            - DCM for rotation from perifocal to geocentric equatorial
Q	            - DCM for rotation from geocentric equatorial into earth-fixed frame
r_rel	        - position vector in earth-fixed frame (km)
alpha	        - satellite right ascension (deg)
delta	        - satellite declination (deg)
n_curves	    - number of curves comprising the ground track plot
ra	            - cell array containing the right ascensions for each of the curves comprising the ground track plot
dec	            - cell array containing the declinations for each of the curves comprising the ground track plot
l, m, n         - direction cosines of r
eps             - a small number below which the eccentricity is considered to be zero
'''

# Constants
mu = 398600                                  # Standard gravitational parameter
J2 = 0.00108263                              # second zonal coefficient
Re = 6378                                    # earth radius
we = (2 * pi + 2 * pi/365.26)/(24 * 3600)    # angular velocity


class Orbit:
    def __init__(*args):
        pass


    def linspace(self, start, stop, n):
        ''' devide the range to n times '''
        h = (stop - start) / (n - 1)
        x = []
        for i in range(n):
            y = start + h * i
            x.append(y)
        return x


    def norm(self, r):
        ''' find the norm of the vector '''
        n = sqrt((r[0]**2) + (r[1]**2) + (r[2] ** 2))
        return n


    def matrix_value(self, matrix):
        ''' find the matrix its determinant value '''
        ele1 = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2])
        ele2 = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2])
        ele3 = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1])
        return ele1 - ele2 + ele3


    def matrix_product(self, matrix1, matrix2):
        ''' matrices product '''
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*matrix2)] for X_row in matrix1]
        return result


    def dot_product(self, a_vector,b_vector):
        ''' vectors dot product '''
        return sum([an * bn for an, bn in zip(a_vector, b_vector)])


    def cross_product(self, a, b):
        ''' vectors cross product '''
        c = [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]
        return c


    def ra_dec_from_r(self, r):
        ''' find right ascension and declination from radius vector '''
        l = r[0]/self.norm(r);
        m = r[1]/self.norm(r);
        n = r[2]/self.norm(r);
        dec = degrees(asin(n))
        if m > 0:
            ra = degrees(acos(l/cos(radians(dec))))
        else:
            ra = 360 - degrees(acos(l/cos(radians(dec))))
        return ra, dec


    def coe_from_sv(self, R, V, mu):
        ''' find orbital elements from raduis vector and velocity '''
        eps = 1.e-10
        r = self.norm(R)
        v = self.norm(V)
        vr = self.dot_product(R, V)/r
        H = self.cross_product(R, V)
        h = self.norm(H)
        incl = acos(H[2]/h)
        N = self.cross_product([0, 0, 1], H)
        n = self.norm(N)
        if n != 0:
            RA = acos(N[0]/n)
        if N[1] < 0:
            RA = 2 * pi - RA
        else:
            RA = 0
        Er = [element * (1/mu * (v ** 2 - mu/r)) for element in R]
        Ev = [element * (1/mu * r * vr) for element in V]
        E = [i - j for i,j in zip(Er, Ev)]
        e = self.norm(E)
        if n != 0:
            if e > eps:
                w = acos(self.dot_product(N, E)/n/e)
                if E[2] < 0:
                    w = 2 * pi - w
            else:
                w = 0
        else:
            w = 0

        if e > eps:
            TA = acos(self.dot_product(E, R)/e/r)
            if vr < 0:
                TA = 2 * pi - TA
        else:
            cp = self.cross_product(N,R)
            if cp[2] >= 0:
                TA = degrees(acos(self.dot_product(N, R)/n/r))
            else:
                TA = degrees(2 * pi - acos(self.dot_product(N, R)/n/r))

        a = (h ** 2)/mu/(1 - e ** 2)
        period = sqrt((4 * (pi ** 2) * (a ** 3))/mu)
        energy = ((v ** 2)/2 - mu/r)
        mean_n = 2 * pi / period
        coe = [a, h, H, e, E, period, energy, mean_n, degrees(incl), degrees(RA), degrees(w), degrees(TA)]
        return coe


    def sv_from_coe(self, h, e, RA, incl, w, TA):
        '''
        find radius vector and velocity from orbital elements
        sv_from_coe(80000, 1.4, 40, 30, 60, 30)
        '''
        RA, incl, w, TA = radians(RA), radians(incl), radians(w), radians(TA)
        rp1 = [element * ((h ** 2)/mu) * (1/(1 + e * cos(TA))) * cos(TA) for element in [1, 0, 0]]
        rp2 = [element * ((h ** 2)/mu) * (1/(1 + e * cos(TA))) * sin(TA) for element in [0, 1, 0]]
        rp = [a + b for a, b in zip(rp1, rp2)]
        vp1 = [element * (mu/h) * (-sin(TA)) for element in [1, 0, 0]]
        vp2 = [element * (mu/h) * (e + cos(TA)) for element in [0, 1, 0]]
        vp = [a + b for a, b in zip(vp1, vp2)]
        R3_W = [ [cos(RA), sin(RA), 0], [-sin(RA), cos(RA), 0], [0, 0, 1]]
        R3_w = [ [cos(w), sin(w), 0], [-sin(w), cos(w), 0], [0, 0, 1]]
        R3_i = [[1, 0, 0], [0, cos(incl), sin(incl)], [0, -sin(incl), cos(incl)]]
        Q_pI = self.matrix_product(R3_w, R3_i)
        Q_pX = self.matrix_product(Q_pI, R3_W)
        r = [sum(a * b for a, b in zip(rp, Y_col)) for Y_col in zip(*Q_pX)]
        v = [sum(a * b for a, b in zip(vp, Y_col)) for Y_col in zip(*Q_pX)]
        return r, v


    def kepler_E(self, e, M):
        ''' iterate kepler equation '''
        error = 1.e-8
        if M < pi:
            E = M + e/2
        else:
            E = M - e/2
        ratio = 1
        while abs(ratio) > error:
            ratio = (E - e * sin(E) - M)/(1 - e * cos(E));
            E = E - ratio
        return E


    def groundtrack(self, rP, rA, Wo, TAo, wpo, incl, n_periods, curve_d):
        '''
        Compute the initial time (since perigee) and the rates of node regression and perigee advance
        returns the right ascension and declination of the ground track
        '''
        Wo, TAo, wpo, incl = radians(Wo), radians(TAo), radians(wpo), radians(incl)
        a = (rA + rP)/2                             #8350
        T = 2 * (pi/sqrt(mu)) * (a ** (3/2))        #7593.4
        e = (rA - rP)/(rA + rP)                     #0.1976
        h = sqrt(mu * a * (1 - e ** 2))             #57691.51
        Eo = 2 * atan(sqrt((1 - e)/(1 + e)) * tan(TAo/2)) #-120.66 rad -2.105
        Mo = Eo - e * sin(radians(Eo))                    #-120.24 rad -2.098
        to = (Mo * T) / (2 * pi)                          #-2536.325
        tf = to + n_periods * T                           #20244.118
        fac = (-3/2 * sqrt(mu) * J2 * (Re ** 2))/(((1 - e ** 2) ** 2) * (a ** (7/2)))   #-8.4e-07
        Wdot = fac * cos(incl)                      #-4.2e-07
        wpdot = fac * (5/2 * (sin(incl) ** 2) - 2)  #1.06e-07
        times = self.linspace(to, tf, curve_d * n_periods)
        ra, dec, theta = [], [], 0
        for i in range(len(times)):
            t = times[i]
            M = 2 * (pi/T) * t
            E = self.kepler_E(e, M)
            TA = 2 * (atan(tan(E/2) * sqrt((1 + e)/(1 - e))))
            r = [element * ((h ** 2)/mu/(1 + e * cos(TA))) for element in [cos(TA), sin(TA), 0]]
            W = Wo + Wdot * t
            wp = wpo + wpdot * t
            R1 = [[cos(W), sin(W), 0], [-sin(W), cos(W), 0], [0, 0, 1]]
            R2 = [[1, 0, 0], [0, cos(incl), sin(incl)], [0, -sin(incl), cos(incl)]]
            R3 = [[cos(wp), sin(wp), 0], [-sin(wp), cos(wp), 0], [0, 0, 1]]
            Qxx = self.matrix_product(R1, R2)
            QxX = self.matrix_product(Qxx, R3)
            R = [sum(a * b for a, b in zip(r, Y_col)) for Y_col in zip(*QxX)]
            theta =  we * (t - to)
            Q = [[cos(theta), sin(theta), 0], [-sin(theta), cos(theta), 0], [0, 0, 1]]
            r_rel = [sum(a * b for a, b in zip(R, Y_col)) for Y_col in zip(*Q)]
            final = self.ra_dec_from_r(r_rel)
            ra.append(final[0])
            dec.append(final[1])
        return ra, dec

