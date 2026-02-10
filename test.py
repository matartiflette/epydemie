import math
import dearpygui.dearpygui as dpg


def compute_bridges(graph):
    # Tarjan: bridges in O(V+E)
    time = 0
    visited = {v: False for v in graph}
    tin = {v: -1 for v in graph}
    low = {v: -1 for v in graph}
    bridges = set()

    def dfs(v, parent):
        nonlocal time
        visited[v] = True
        tin[v] = time
        low[v] = time
        time += 1
        for to in graph[v]:
            if to == parent:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.add(tuple(sorted((v, to))))

    for v in graph:
        if not visited[v]:
            dfs(v, None)
    return bridges


def circular_layout(nodes, center=(350, 250), radius=180):
    n = len(nodes)
    positions = {}
    for i, node in enumerate(nodes):
        angle = (2 * math.pi * i) / max(n, 1)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        positions[node] = (x, y)
    return positions


def draw_graph(drawlist_id, graph, positions, bridges):
    dpg.delete_item(drawlist_id, children_only=True)

    # Draw edges
    for a in graph:
        for b in graph[a]:
            if a < b:  # avoid duplicates
                ax, ay = positions[a]
                bx, by = positions[b]
                is_bridge = tuple(sorted((a, b))) in bridges
                color = (220, 60, 60, 255) if is_bridge else (120, 120, 120, 255)
                thickness = 4 if is_bridge else 2
                dpg.draw_line((ax, ay), (bx, by), color=color, thickness=thickness, parent=drawlist_id)

    # Draw nodes
    for node, (x, y) in positions.items():
        dpg.draw_circle((x, y), 18, color=(30, 30, 30, 255), fill=(240, 240, 240, 255), parent=drawlist_id)
        dpg.draw_text((x - 6, y - 8), node, color=(20, 20, 20, 255), size=16, parent=drawlist_id)


def main():
    # Example graph
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B"],
        "D": ["B", "E", "F"],
        "E": ["D", "F"],
        "F": ["D", "E", "G"],
        "G": ["F"],
    }

    nodes = list(graph.keys())
    positions = circular_layout(nodes)
    bridges = compute_bridges(graph)

    dpg.create_context()
    dpg.create_viewport(title="Graph: liens et ponts", width=700, height=520)

    with dpg.window(label="Visualisation", width=700, height=520):
        dpg.add_text("Liens gris, ponts en rouge.")
        drawlist_id = dpg.add_drawlist(width=680, height=450)

    draw_graph(drawlist_id, graph, positions, bridges)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
