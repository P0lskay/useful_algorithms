def best_solve(mid, volume, vol, rest):
    global v
    '''
    :param mid: the mid is list of prices per liter
    :type mid: list
    :param volume: the volume is list of volume of subjects
    :type volume: list
    :param vol: v is free volume of backpack right now
    :type vol: int
    :param rest: res is count of subjects in backpack right now
    :type rest: float
    :return rest
    '''
    if v > vol and mid:
        t = max(enumerate(mid), key=lambda x: x[1]) # t = [index, value]
        g = v-vol
        if volume[t[0]] >= g:
            rest += t[1]*g
            vol+=g
            return rest
        else:
            rest += volume[t[0]] * t[1]
            vol += volume[t[0]]
            del volume[t[0]]
            del mid[t[0]]
            rest = best_solve(mid, volume, vol, rest)
    return rest


n, v = map(int, input().split())
res = 0.0
v_now = 0
arr_w = []
arr_sr = []
for i in range(n):
    c, w = map(int, input().split())
    arr_w.append(w)
    arr_sr.append(c / w)
print('%.3f' % best_solve(arr_sr, arr_w, v_now, res))