def header_params(params):
    dict_params = {}
    # 将params分隔为列表
    header_list = params.split('&')
    for i in header_list:
        # 将列表中的值分割为key/valse形式
        line_list = i.split('=')
        dict_params[line_list[0]] = line_list[1]
    return dict_params
