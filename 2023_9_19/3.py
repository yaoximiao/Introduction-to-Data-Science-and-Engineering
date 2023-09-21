def judgment(state):
    if state[0] == state[1] and state[2] == state[3]:
        return False
    elif state[0] == state[2] and state[1] == state[3]:
        return False
    elif state[0] != state[1] and state[1] == state[2] and state[2] == state[3]:
        return False
    else:
        return True


step = 0


def nextstep(state, record, action):
    global step
    now = state[0] * 8 + state[1] * 4 + state[2] * 2 + state[3] * 1
    if now == 15:
        return
    if state[0] == 1:
        for i in range(0, 4):
            if i == 0:
                change_state = now - (-1) ** (state[0] + 1) * 8
                if record[change_state] == 0:
                    state[i] = 1 - state[i]
                    record[change_state] = 1
                    action[step] = change_state
                    step += 1
                    nextstep(state, record, action)
            if i > 0:
                change_state = now - (-1) ** (state[0] + 1) * 8 - (-1) ** (state[i] + 1) * 2 ** (3 - i)
                if state[i] == state[0] and record[change_state] == 0:
                    state[i] = 1 - state[i]
                    state[0] = 1 - state[0]
                    record[change_state] = 1
                    action[step] = change_state
                    step += 1
                    nextstep(state, record, action)
