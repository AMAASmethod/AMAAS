import os
import pandas as pd

from get_action_from_log import process_file, process_file_merge
from file_to_hashcode import get_code
from repair_action import repair_action_text
from delete_same_page import remain
from graph import get_graph
from action_xml_replace import xml_replace
from frequent_node_count import get_node_count
from most_node_action_path import node_action_path
from get_related_path import get_related
from shortest_node_path import get_shortest_path
from landmark import get_landmark
from bounds import get_bounds
from path import get_path
from map import create_map
from evaluation_image_label import run_image_no_label_path_evaluation, checked_node_image, unchecked_node_image, shortest_paths_image
from evaluation_no_label import run_no_label_path_evaluation, checked_node_no_label, unchecked_node_no_label, shortest_paths_no_label
from evaluation_false_label import run_false_label_path_evaluation, checked_node_false, unchecked_node_false, shortest_paths_false
from evaluation_scattered_focus import checked_node_focus, unchecked_node_focus, shortest_paths_focus, inversions_in_xml_bounds
from evaluation import eva


def main():
    folder_path = r"E:\Fastbot_Android-main\fastbot-reddit"
    input_file = os.path.join(folder_path, 'Logcat.txt')
    out_action_file = os.path.join(folder_path, 'action.txt')
    out_code_file = os.path.join(folder_path, 'file_hashes.txt')
    out_repair_file = os.path.join(folder_path, 'action_repair.txt')
    out_remain_file = os.path.join(folder_path, 'action_remain.txt')

    cycles_file = os.path.join(folder_path, 'cycles.txt')
    replace_xml_file = os.path.join(folder_path, 'replace_xml.txt')
    node_file = os.path.join(folder_path, 'nodes.txt')
    edge_file = os.path.join(folder_path, 'edges.txt')
    graph_file = os.path.join(folder_path, 'graph1.html')

    out_repair_new_file = os.path.join(folder_path, 'action_repair_new.txt')
    out_keywords_file = os.path.join(folder_path, 'any-node.txt')

    output_action_file = os.path.join(folder_path, 'related_page.txt')
    output_action_file1 = os.path.join(folder_path, 'related_page1.txt')
    output_action_file2 = os.path.join(folder_path, 'related_page2.txt')
    output_action_file3 = os.path.join(folder_path, 'related_page3.txt')

    out_node_file = os.path.join(folder_path, 'related_path.txt')
    out_node_file1 = os.path.join(folder_path, 'related_path1.txt')
    out_node_file2 = os.path.join(folder_path, 'related_path2.txt')
    out_node_file3 = os.path.join(folder_path, 'related_path3.txt')

    shortest_path_file = os.path.join(folder_path, 'shortest_path.txt')
    shortest_path_xml_file = os.path.join(folder_path, 'shortest_path_xml.txt')
    shortest_path_file1 = os.path.join(folder_path, 'shortest_path1.txt')
    shortest_path_xml_file1 = os.path.join(folder_path, 'shortest_path_xml1.txt')
    shortest_path_file2 = os.path.join(folder_path, 'shortest_path2.txt')
    shortest_path_xml_file2 = os.path.join(folder_path, 'shortest_path_xml2.txt')
    shortest_path_file3 = os.path.join(folder_path, 'shortest_path3.txt')
    shortest_path_xml_file3 = os.path.join(folder_path, 'shortest_path_xml3.txt')

    process_file_merge(input_file)
    process_file(input_file, out_action_file)
    get_code(folder_path, out_code_file)
    repair_action_text(folder_path, out_action_file, out_repair_file)
    remain(folder_path, out_repair_file, out_remain_file)
    get_graph(folder_path, out_code_file, cycles_file, replace_xml_file, node_file, edge_file, graph_file)
    xml_replace(out_remain_file, replace_xml_file, out_repair_new_file)
    get_node_count(out_repair_new_file, out_keywords_file)

    node_action_path(out_keywords_file, out_repair_new_file, output_action_file, edge_file, 0, 0.25)
    node_action_path(out_keywords_file, out_repair_new_file, output_action_file1, edge_file, 0.25, 0.5)
    node_action_path(out_keywords_file, out_repair_new_file, output_action_file2, edge_file, 0.5, 0.75)
    node_action_path(out_keywords_file, out_repair_new_file, output_action_file3, edge_file, 0.75, 1.0)

    get_related(output_action_file, out_node_file)
    get_related(output_action_file1, out_node_file1)
    get_related(output_action_file2, out_node_file2)
    get_related(output_action_file3, out_node_file3)

    get_shortest_path(folder_path, edge_file, out_node_file, shortest_path_file, shortest_path_xml_file)
    get_shortest_path(folder_path, edge_file, out_node_file1, shortest_path_file1, shortest_path_xml_file1)
    get_shortest_path(folder_path, edge_file, out_node_file2, shortest_path_file2, shortest_path_xml_file2)
    get_shortest_path(folder_path, edge_file, out_node_file3, shortest_path_file3, shortest_path_xml_file3)

    landmark_path = os.path.join(folder_path, 'landmark.txt')
    get_landmark(folder_path, landmark_path)

    xml_file_input = os.path.join(folder_path, 'shortest_path_xml.txt')
    bounds_file_output = os.path.join(folder_path, 'bounds.txt')
    xml_file_input1 = os.path.join(folder_path, 'shortest_path_xml1.txt')
    bounds_file_output1 = os.path.join(folder_path, 'bounds1.txt')
    xml_file_input2 = os.path.join(folder_path, 'shortest_path_xml2.txt')
    bounds_file_output2 = os.path.join(folder_path, 'bounds2.txt')
    xml_file_input3 = os.path.join(folder_path, 'shortest_path_xml3.txt')
    bounds_file_output3 = os.path.join(folder_path, 'bounds3.txt')
    get_bounds(landmark_path, xml_file_input, bounds_file_output)
    get_bounds(landmark_path, xml_file_input1, bounds_file_output1)
    get_bounds(landmark_path, xml_file_input2, bounds_file_output2)
    get_bounds(landmark_path, xml_file_input3, bounds_file_output3)

    input_bounds_file = os.path.join(folder_path, 'bounds.txt')
    final_path_file = os.path.join(folder_path, 'path.txt')
    input_bounds_file1 = os.path.join(folder_path, 'bounds1.txt')
    final_path_file1 = os.path.join(folder_path, 'path1.txt')
    input_bounds_file2 = os.path.join(folder_path, 'bounds2.txt')
    final_path_file2 = os.path.join(folder_path, 'path2.txt')
    input_bounds_file3 = os.path.join(folder_path, 'bounds3.txt')
    final_path_file3 = os.path.join(folder_path, 'path3.txt')
    get_path(folder_path, out_repair_new_file, input_bounds_file, final_path_file)
    get_path(folder_path, out_repair_new_file, input_bounds_file1, final_path_file1)
    get_path(folder_path, out_repair_new_file, input_bounds_file2, final_path_file2)
    get_path(folder_path, out_repair_new_file, input_bounds_file3, final_path_file3)

    create_map(folder_path)
    file_name = "color_path_blue_xml.txt"
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        xml_file_input = os.path.join(folder_path, 'color_path_blue_xml.txt')
        bounds_file_output = os.path.join(folder_path, 'bounds_blue.txt')
        xml_file_input1 = os.path.join(folder_path, 'color_path_green_xml.txt')
        bounds_file_output1 = os.path.join(folder_path, 'bounds_green.txt')
        xml_file_input2 = os.path.join(folder_path, 'color_path_purple_xml.txt')
        bounds_file_output2 = os.path.join(folder_path, 'bounds_purple.txt')
        get_bounds(landmark_path, xml_file_input, bounds_file_output)
        get_bounds(landmark_path, xml_file_input1, bounds_file_output1)
        get_bounds(landmark_path, xml_file_input2, bounds_file_output2)

    file_name = "bounds_blue.txt"
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        input_bounds_file = os.path.join(folder_path, 'bounds_blue.txt')
        final_path_file_blue = os.path.join(folder_path, 'path_blue.txt')
        input_bounds_file1 = os.path.join(folder_path, 'bounds_green.txt')
        final_path_file_green = os.path.join(folder_path, 'path_green.txt')
        input_bounds_file2 = os.path.join(folder_path, 'bounds_purple.txt')
        final_path_file_purple = os.path.join(folder_path, 'path_purple.txt')
        get_path(folder_path, out_repair_new_file, input_bounds_file, final_path_file_blue)
        get_path(folder_path, out_repair_new_file, input_bounds_file1, final_path_file_green)
        get_path(folder_path, out_repair_new_file, input_bounds_file2, final_path_file_purple)

    final_path_file = os.path.join(folder_path, 'path.txt')
    final_path_file_blue = os.path.join(folder_path, 'path_blue.txt')
    final_path_file_green = os.path.join(folder_path, 'path_green.txt')
    final_path_file_purple = os.path.join(folder_path, 'path_purple.txt')
    output_no_label_file = os.path.join(folder_path, 'evaluation_no_label_path.txt')
    output_no_label_b_file = os.path.join(folder_path, 'evaluation_no_label_path_b.txt')
    output_no_label_g_file = os.path.join(folder_path, 'evaluation_no_label_path_g.txt')
    output_no_label_pur_file = os.path.join(folder_path, 'evaluation_no_label_path_pur.txt')
    unchecked_no_label_output = os.path.join(folder_path, 'evaluation_no_label_unchecked_path.txt')
    checked_node_no_label(shortest_path_file)
    checked_node_no_label(shortest_path_file1)
    checked_node_no_label(shortest_path_file2)
    checked_node_no_label(shortest_path_file3)
    a1 = run_no_label_path_evaluation(final_path_file, output_no_label_file)
    a2 = run_no_label_path_evaluation(final_path_file_blue, output_no_label_b_file)
    a3 = run_no_label_path_evaluation(final_path_file_green, output_no_label_g_file)
    a4 = run_no_label_path_evaluation(final_path_file_purple, output_no_label_pur_file)
    a5 = unchecked_node_no_label(shortest_paths_no_label, folder_path, replace_xml_file, unchecked_no_label_output)

    output_image_file = os.path.join(folder_path, 'evaluation_image_no_label_path.txt')
    output_image_b_file = os.path.join(folder_path, 'evaluation_image_no_label_path_b.txt')
    output_image_g_file = os.path.join(folder_path, 'evaluation_image_no_label_path_g.txt')
    output_image_pur_file = os.path.join(folder_path, 'evaluation_image_no_label_path_pur.txt')
    unchecked_image_output = os.path.join(folder_path, 'evaluation_image_no_label_unchecked_path.txt')
    checked_node_image(shortest_path_file)
    checked_node_image(shortest_path_file1)
    checked_node_image(shortest_path_file2)
    checked_node_image(shortest_path_file3)
    b1 = run_image_no_label_path_evaluation(final_path_file, output_image_file)
    b2 = run_image_no_label_path_evaluation(final_path_file_blue, output_image_b_file)
    b3 = run_image_no_label_path_evaluation(final_path_file_green, output_image_g_file)
    b4 = run_image_no_label_path_evaluation(final_path_file_purple, output_image_pur_file)
    b5 = unchecked_node_image(shortest_paths_image, folder_path, replace_xml_file, unchecked_image_output)

    output_false_file = os.path.join(folder_path, 'evaluation_false_label_path.txt')
    output_false_b_file = os.path.join(folder_path, 'evaluation_false_label_path_b.txt')
    output_false_g_file = os.path.join(folder_path, 'evaluation_false_label_path_g.txt')
    output_false_pur_file = os.path.join(folder_path, 'evaluation_false_label_path_pur.txt')
    unchecked_false_output = os.path.join(folder_path, 'evaluation_false_label_unchecked_path.txt')
    checked_node_false(shortest_path_file)
    checked_node_false(shortest_path_file1)
    checked_node_false(shortest_path_file2)
    checked_node_false(shortest_path_file3)
    c1 = run_false_label_path_evaluation(final_path_file, output_false_file)
    c2 = run_false_label_path_evaluation(final_path_file_blue, output_false_b_file)
    c3 = run_false_label_path_evaluation(final_path_file_green, output_false_g_file)
    c4 = run_false_label_path_evaluation(final_path_file_purple, output_false_pur_file)
    c5 = unchecked_node_false(shortest_paths_false, folder_path, replace_xml_file, unchecked_false_output)

    bounds_file_path = os.path.join(folder_path, 'bounds.txt')
    output_focus_file = os.path.join(folder_path, 'evaluation_inversion_ratio.txt')
    bounds_file_path_blue = os.path.join(folder_path, 'bounds_blue.txt')
    output_focus_blue = os.path.join(folder_path, 'evaluation_inversion_ratio_blue.txt')
    bounds_file_path_green = os.path.join(folder_path, 'bounds_green.txt')
    output_focus_green = os.path.join(folder_path, 'evaluation_inversion_ratio_green.txt')
    bounds_file_path_purple = os.path.join(folder_path, 'bounds_purple.txt')
    output_focus_purple = os.path.join(folder_path, 'evaluation_inversion_ratio_purple.txt')
    unchecked_focus_output = os.path.join(folder_path, 'evaluation_inversion_ratio_unchecked_path.txt')
    checked_node_focus(shortest_path_file)
    checked_node_focus(shortest_path_file1)
    checked_node_focus(shortest_path_file2)
    checked_node_focus(shortest_path_file3)
    d1 = inversions_in_xml_bounds(bounds_file_path, folder_path, output_focus_file)
    d2 = inversions_in_xml_bounds(bounds_file_path_blue, folder_path, output_focus_blue)
    d3 = inversions_in_xml_bounds(bounds_file_path_green, folder_path, output_focus_green)
    d4 = inversions_in_xml_bounds(bounds_file_path_purple, folder_path, output_focus_purple)
    d5 = unchecked_node_focus(shortest_paths_focus, folder_path, replace_xml_file, unchecked_focus_output)

    def write_values_to_file(file_path, *values):
        with open(file_path, 'a') as file:
            for value in values:
                file.write(f'{value}\n')

    def read_values_from_file(file_path):
        variables = {'a': [], 'b': [], 'c': [], 'd': []}
        with open(file_path, 'r') as file:
            lines = file.readlines()
            variables['a'] = [float(line.strip()) for line in lines[:5]]
            variables['b'] = [float(line.strip()) for line in lines[5:10]]
            variables['c'] = [float(line.strip()) for line in lines[10:15]]
            variables['d'] = [float(line.strip()) for line in lines[15:20]]
        return variables

    value_path = os.path.join(folder_path, 'e-value.txt')

    write_values_to_file(value_path, a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, c1, c2, c3, c4, c5, d1, d2, d3, d4, d5)
    variables = read_values_from_file(value_path)
    print(variables)

    for key in variables:
        value = 0.9 * variables[key][0] + 0.04 * variables[key][1] + 0.03 * variables[key][2] + 0.02 * variables[key][3] + 0.01 * variables[key][4]
        if value == 0:
            value = 1e-8
        variables[key] = value
    print(variables[key])

    a, b, c, d = variables['a'], variables['b'], variables['c'], variables['d']

    part_after_fastbot = folder_path.split("fastbot-")[-1]
    excel_path = r'E:\Fastbot_Android-main\eval.xlsx'
    data = pd.read_excel(excel_path, usecols='A:E')
    new_row = {'App': part_after_fastbot, 'A1(No label)': a, 'A2(Image with no description)': b, 'A3(False label)': c, 'A4(Focus disorder)': d}
    new_row_df = pd.DataFrame([new_row])
    data = pd.concat([data, new_row_df], ignore_index=True)
    data.to_excel(excel_path, index=False)
    eva(data)


if __name__ == "__main__":
    main()
