fetch 6wa1
remove solvent

color cyan, chain A
color lightmagneta, chain B

hide cartoon
show sphere, name CA

distance edges_A, (chain A and name CA), (chain A and name CA), 8
set dash_gap, 0, edges_A
set dash_radius, 0.06, edges_A
color lightteal, edges_A


distance edges_B, (chain B and name CA), (chain B and name CA), 8
hide labels, edges_B
set dash_gap, 0, edges_B
set dash_radius, 0.06, edges_B
color salmon, edges_B

distance edges_AB, (chain A and name CA), (chain B and name CA), 8
hide labels, edges_AB
set dash_gap, 0, edges_AB
set dash_radius, 0.08, edges_AB
color white, edges_AB   # neon pop


bg_color black
set sphere_scale, 0.75
set ray_trace_mode, 1
set specular, 0.6
set shininess, 80
set dash_gap, 0
set depth_cue, off
set fog, off
set dash_radius, 0.18
set ray_shadow, off
set ray_trace_gain, 2
set gamma, 1.2
set antialias, 2


set ray_opaque_background, on
png neon_edges.png, dpi=600
