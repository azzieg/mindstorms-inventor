# Word Blocks Python reference

In the following snippets, the `vm` variable is a reference to a VirtualMachine
instance and the `await` keyword can only be used in async functions. Please
read the [introduction](/README.md) to learn about the basic setup necessary to
run such code on a LEGO hub.

## Motors

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/01_motors/01a_motor_run_for_angle.png" width="286"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01_motors/01a_motor_run_for_angle.py#L1-L11 |
| <img src="/word_blocks/01_motors/01b_motor_run_for_time.png" width="281"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01_motors/01b_motor_run_for_time.py#L1-L11 |
| <img src="/word_blocks/01_motors/02_motor_run_to_position.png" width="309"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01_motors/02_motor_run_to_position.py#L1-L12 |
| <img src="/word_blocks/01_motors/03_motor_start.png" width="194"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01_motors/03_motor_start.py#L1-L7 |
| <img src="/word_blocks/01_motors/04_motor_stop.png" width="150"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01_motors/04_motor_stop.py#L1-L2 |
| <img src="/word_blocks/01_motors/05_motor_set_speed.png" width="206"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01_motors/05_motor_set_speed.py#L1-L2 |
| <img src="/word_blocks/01_motors/06_motor_get_position.png" width="143"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01_motors/06_motor_get_position.py#L1-L10 |
| <img src="/word_blocks/01_motors/07_motor_get_speed.png" width="133"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01_motors/07_motor_get_speed.py#L1-L7 |

## More Motors

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/01x_more_motors/01a_motor_run_for_angle_at_speed.png" width="340"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/01a_motor_run_for_angle_at_speed.py#L1-L11 |
| <img src="/word_blocks/01x_more_motors/01b_motor_run_for_time_at_speed.png" width="336"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/01b_motor_run_for_time_at_speed.py#L1-L11 |
| <img src="/word_blocks/01x_more_motors/02_motor_start_at_speed.png" width="248"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/02_motor_start_at_speed.py#L1-L7 |
| <img src="/word_blocks/01x_more_motors/03_motor_run_to_relative_position_at_speed.png" width="344"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/03_motor_run_to_relative_position_at_speed.py#L1-L11 |
| <img src="/word_blocks/01x_more_motors/04_motor_set_relative_position.png" width="241"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/04_motor_set_relative_position.py#L1-L2 |
| <img src="/word_blocks/01x_more_motors/05_motor_get_relative_position.png" width="184"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/05_motor_get_relative_position.py#L1-L7 |
| <img src="/word_blocks/01x_more_motors/06_motor_start_at_power.png" width="249"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/06_motor_start_at_power.py#L1-L4 |
| <img src="/word_blocks/01x_more_motors/07_motor_get_power.png" width="133"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/07_motor_get_power.py#L1-L7 |
| <img src="/word_blocks/01x_more_motors/08_motor_set_at_stop.png" width="268"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/08_motor_set_at_stop.py#L1-L2 |
| <img src="/word_blocks/01x_more_motors/09_motor_set_acceleration.png" width="272"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/09_motor_set_acceleration.py#L1-L4 |
| <img src="/word_blocks/01x_more_motors/10_motor_set_stall_detection.png" width="238"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/10_motor_set_stall_detection.py#L1-L2 |
| <img src="/word_blocks/01x_more_motors/11_motor_was_interrupted.png" width="254"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/01x_more_motors/11_motor_was_interrupted.py#L1-L5 |

## Movement

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/02_movement/01a_motors_move_distance.png" width="225"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/01a_motors_move_distance.py#L1-L16 |
| <img src="/word_blocks/02_movement/01b_motors_move_angle.png" width="256"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/01b_motors_move_angle.py#L1-L9 |
| <img src="/word_blocks/02_movement/01c_motors_move_time.png" width="251"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/01c_motors_move_time.py#L1-L9 |
| <img src="/word_blocks/02_movement/02a_motors_steer_distance.png" width="256"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/02a_motors_steer_distance.py#L1-L17 |
| <img src="/word_blocks/02_movement/02b_motors_steer_angle.png" width="277"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/02b_motors_steer_angle.py#L1-L10 |
| <img src="/word_blocks/02_movement/02c_motors_steer_time.png" width="272"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/02c_motors_steer_time.py#L1-L10 |
| <img src="/word_blocks/02_movement/03_motors_start_steering.png" width="190"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/03_motors_start_steering.py#L1-L9 |
| <img src="/word_blocks/02_movement/04_motors_stop.png" width="116"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/04_motors_stop.py#L1-L4 |
| <img src="/word_blocks/02_movement/05_motors_set_speed.png" width="223"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/05_motors_set_speed.py#L1-L2 |
| <img src="/word_blocks/02_movement/06_motors_set_ports.png" width="236"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/06_motors_set_ports.py#L1-L2 |
| <img src="/word_blocks/02_movement/07_motors_calibrate_distance.png" width="292"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02_movement/07_motors_calibrate_distance.py#L1-L2 |

## More Movement

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/02x_more_movement/01a_motors_move_distance_at_speed.png" width="312"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/01a_motors_move_distance_at_speed.py#L1-L15 |
| <img src="/word_blocks/02x_more_movement/01b_motors_move_angle_at_speed.png" width="348"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/01b_motors_move_angle_at_speed.py#L1-L8 |
| <img src="/word_blocks/02x_more_movement/01c_motors_move_time_at_speed.png" width="344"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/01c_motors_move_time_at_speed.py#L1-L8 |
| <img src="/word_blocks/02x_more_movement/02_motors_start_at_speed.png" width="251"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/02_motors_start_at_speed.py#L1-L7 |
| <img src="/word_blocks/02x_more_movement/03a_motors_steer_distance_at_speed.png" width="355"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/03a_motors_steer_distance_at_speed.py#L1-L17 |
| <img src="/word_blocks/02x_more_movement/03b_motors_streer_angle_at_speed.png" width="389"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/03b_motors_streer_angle_at_speed.py#L1-L10 |
| <img src="/word_blocks/02x_more_movement/03c_motors_streer_time_at_speed.png" width="380"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/03c_motors_streer_time_at_speed.py#L1-L10 |
| <img src="/word_blocks/02x_more_movement/04_motors_start_steering_at_speed.png" width="276"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/04_motors_start_steering_at_speed.py#L1-L9 |
| <img src="/word_blocks/02x_more_movement/05_motors_start_at_power.png" width="252"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/05_motors_start_at_power.py#L1-L4 |
| <img src="/word_blocks/02x_more_movement/06_motors_start_steering_at_power.png" width="290"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/06_motors_start_steering_at_power.py#L1-L9 |
| <img src="/word_blocks/02x_more_movement/07_motors_set_at_stop.png" width="285"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/07_motors_set_at_stop.py#L1-L2 |
| <img src="/word_blocks/02x_more_movement/08_motors_set_acceleration.png" width="260"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/08_motors_set_acceleration.py#L1-L4 |
| <img src="/word_blocks/02x_more_movement/09_motors_were_interrupted.png" width="217"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/02x_more_movement/09_motors_were_interrupted.py#L1-L5 |

## Light

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/03_light/01_matrix_start_animation.png" width="220"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/01_matrix_start_animation.py#L1-L18 |
| <img src="/word_blocks/03_light/02_matrix_play_animation.png" width="246"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/02_matrix_play_animation.py#L1-L16 |
| <img src="/word_blocks/03_light/03_matrix_display_for_time.png" width="243"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/03_matrix_display_for_time.py#L1-L11 |
| <img src="/word_blocks/03_light/04_matrix_display.png" width="141"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/04_matrix_display.py#L1-L10 |
| <img src="/word_blocks/03_light/05_matrix_write.png" width="125"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/05_matrix_write.py#L1-L2 |
| <img src="/word_blocks/03_light/06_matrix_clear.png" width="123"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/06_matrix_clear.py#L1-L4 |
| <img src="/word_blocks/03_light/07_matrix_set_brightness.png" width="216"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/07_matrix_set_brightness.py#L1-L2 |
| <img src="/word_blocks/03_light/08_matrix_set_pixel.png" width="261"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/08_matrix_set_pixel.py#L1-L7 |
| <img src="/word_blocks/03_light/09_matrix_rotate_orientation.png" width="186"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/09_matrix_rotate_orientation.py#L1-L4 |
| <img src="/word_blocks/03_light/10_matrix_set_orientation.png" width="212"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/10_matrix_set_orientation.py#L1-L5 |
| <img src="/word_blocks/03_light/11_button_set_color.png" width="227"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/11_button_set_color.py#L1-L9 |
| <img src="/word_blocks/03_light/12_ultrasonic_set_lights.png" width="184"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/03_light/12_ultrasonic_set_lights.py#L1-L14 |

## Sound

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/04_sound/01_speaker_play_sound.png" width="190"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/01_speaker_play_sound.py#L1-L10 |
| <img src="/word_blocks/04_sound/02_speaker_start_sound.png" width="137"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/02_speaker_start_sound.py#L1-L10 |
| <img src="/word_blocks/04_sound/03_speaker_play_beep.png" width="239"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/03_speaker_play_beep.py#L1-L5 |
| <img src="/word_blocks/04_sound/04_speaker_start_beep.png" width="178"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/04_speaker_start_beep.py#L1-L6 |
| <img src="/word_blocks/04_sound/05_speaker_stop.png" width="91"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/05_speaker_stop.py#L1-L3 |
| <img src="/word_blocks/04_sound/06a_speaker_change_pitch.png" width="193"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/06a_speaker_change_pitch.py#L1-L9 |
| <img src="/word_blocks/04_sound/06b_speaker_change_pan.png" width="244"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/06b_speaker_change_pan.py#L1-L9 |
| <img src="/word_blocks/04_sound/07a_speaker_set_pitch.png" width="184"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/07a_speaker_set_pitch.py#L1-L2 |
| <img src="/word_blocks/04_sound/07b_speaker_set_pan.png" width="225"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/07b_speaker_set_pan.py#L1-L2 |
| <img src="/word_blocks/04_sound/08_speaker_clear_effects.png" width="112"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/08_speaker_clear_effects.py#L1-L3 |
| <img src="/word_blocks/04_sound/09_speaker_change_volume.png" width="143"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/09_speaker_change_volume.py#L1-L9 |
| <img src="/word_blocks/04_sound/10_speaker_set_volume.png" width="131"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/10_speaker_set_volume.py#L1-L4 |
| <img src="/word_blocks/04_sound/11_speaker_get_volume.png" width="56"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/04_sound/11_speaker_get_volume.py#L1 |

## Events

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/05_events/01_program_on_start.png" width="161"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/01_program_on_start.py#L1-L5 |
| <img src="/word_blocks/05_events/02_optical_on_color.png" width="206"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/02_optical_on_color.py#L1-L21 |
| <img src="/word_blocks/05_events/03a_force_on_pressed.png" width="196"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/03a_force_on_pressed.py#L1-L15 |
| <img src="/word_blocks/05_events/03b_force_on_hard_pressed.png" width="222"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/03b_force_on_hard_pressed.py#L1-L15 |
| <img src="/word_blocks/05_events/03c_force_on_released.png" width="198"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/03c_force_on_released.py#L1-L24 |
| <img src="/word_blocks/05_events/03d_force_on_changed.png" width="247"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/03d_force_on_changed.py#L1-L22 |
| <img src="/word_blocks/05_events/04_ultrasonic_on_distance.png" width="295"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/04_ultrasonic_on_distance.py#L1-L17 |
| <img src="/word_blocks/05_events/05_imu_on_orientation.png" width="168"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/05_imu_on_orientation.py#L1-L9 |
| <img src="/word_blocks/05_events/06_imu_on_gesture.png" width="151"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/06_imu_on_gesture.py#L1-L8 |
| <img src="/word_blocks/05_events/07_button_on_action.png" width="251"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/07_button_on_action.py#L1-L9 |
| <img src="/word_blocks/05_events/08_program_on_condition.png" width="78"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/08_program_on_condition.py#L1-L8 |
| <img src="/word_blocks/05_events/09_messages_on_broadcast.png" width="166"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/09_messages_on_broadcast.py#L1-L5 |
| <img src="/word_blocks/05_events/10_messages_send_broadcast.png" width="144"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/10_messages_send_broadcast.py#L1-L3 |
| <img src="/word_blocks/05_events/11_messages_send_broadcast_and_wait.png" width="193"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/11_messages_send_broadcast_and_wait.py#L1-L4 |
| <img src="/word_blocks/05_events/12_program_on_timer.png" width="113"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/05_events/12_program_on_timer.py#L1-L10 |

## Control

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/06_control/01_control_wait_time.png" width="116"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/01_control_wait_time.py#L1-L2 |
| <img src="/word_blocks/06_control/02_control_wait_until.png" width="97"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/02_control_wait_until.py#L1-L6 |
| <img src="/word_blocks/06_control/03_control_repeat_n.png" width="110"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/03_control_repeat_n.py#L1-L3 |
| <img src="/word_blocks/06_control/04_control_forever.png" width="110"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/04_control_forever.py#L1-L3 |
| <img src="/word_blocks/06_control/05_control_repeat_until.png" width="110"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/05_control_repeat_until.py#L1-L6 |
| <img src="/word_blocks/06_control/06_control_if.png" width="110"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/06_control_if.py#L1-L3 |
| <img src="/word_blocks/06_control/07_control_if_else.png" width="110"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/07_control_if_else.py#L1-L5 |
| <img src="/word_blocks/06_control/08_control_fork.png" width="110"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/08_control_fork.py#L1-L11 |
| <img src="/word_blocks/06_control/09_control_stop_others.png" width="104"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/09_control_stop_others.py#L1-L5 |
| <img src="/word_blocks/06_control/10a_control_stop_all.png" width="81"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/10a_control_stop_all.py#L1-L7 |
| <img src="/word_blocks/06_control/10b_control_stop_this.png" width="119"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/10b_control_stop_this.py#L1-L5 |
| <img src="/word_blocks/06_control/10c_control_stop_and_exit.png" width="159"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/06_control/10c_control_stop_and_exit.py#L1-L3 |

## Sensors

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/07_sensors/01_optical_is_color.png" width="205"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/01_optical_is_color.py#L1-L15 |
| <img src="/word_blocks/07_sensors/02_optical_get_color.png" width="127"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/02_optical_get_color.py#L1-L12 |
| <img src="/word_blocks/07_sensors/03_optical_is_reflective.png" width="259"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/03_optical_is_reflective.py#L1-L8 |
| <img src="/word_blocks/07_sensors/04_optical_get_reflection.png" width="173"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/04_optical_get_reflection.py#L1-L8 |
| <img src="/word_blocks/07_sensors/05_ultrasonic_is_distance.png" width="307"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/05_ultrasonic_is_distance.py#L1-L10 |
| <img src="/word_blocks/07_sensors/06_ultrasonic_get_distance.png" width="208"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/06_ultrasonic_get_distance.py#L1-L10 |
| <img src="/word_blocks/07_sensors/07_imu_get_gesture.png" width="99"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/07_imu_get_gesture.py#L1-L5 |
| <img src="/word_blocks/07_sensors/08_imu_is_gesture.png" width="162"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/08_imu_is_gesture.py#L1-L3 |
| <img src="/word_blocks/07_sensors/09_imu_is_orientation.png" width="163"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/09_imu_is_orientation.py#L1-L5 |
| <img src="/word_blocks/07_sensors/10_imu_get_orientation.png" width="116"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/10_imu_get_orientation.py#L1-L5 |
| <img src="/word_blocks/07_sensors/11_imu_reset_yaw.png" width="146"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/11_imu_reset_yaw.py#L1-L7 |
| <img src="/word_blocks/07_sensors/12_button_is_pressed.png" width="262"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/12_button_is_pressed.py#L1-L4 |
| <img src="/word_blocks/07_sensors/13_imu_get_angle.png" width="147"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/13_imu_get_angle.py#L1-L5 |
| <img src="/word_blocks/07_sensors/14_program_get_timer.png" width="86"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/14_program_get_timer.py#L1-L2 |
| <img src="/word_blocks/07_sensors/15_program_reset_timer.png" width="107"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07_sensors/15_program_reset_timer.py#L1-L2 |

## More Sensors

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/07x_more_sensors/01_optical_get_raw_color.png" width="171"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/01_optical_get_raw_color.py#L1-L12 |
| <img src="/word_blocks/07x_more_sensors/02a_force_is_pressed.png" width="207"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/02a_force_is_pressed.py#L1-L8 |
| <img src="/word_blocks/07x_more_sensors/02b_force_is_hard_pressed.png" width="233"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/02b_force_is_hard_pressed.py#L1-L8 |
| <img src="/word_blocks/07x_more_sensors/03_force_get_force.png" width="233"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/03_force_get_force.py#L1-L8 |
| <img src="/word_blocks/07x_more_sensors/04_imu_get_acceleration.png" width="164"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/04_imu_get_acceleration.py#L1-L5 |
| <img src="/word_blocks/07x_more_sensors/05_imu_get_angular_velocity.png" width="181"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/05_imu_get_angular_velocity.py#L1-L4 |
| <img src="/word_blocks/07x_more_sensors/06_optical_set_mode.png" width="225"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/06_optical_set_mode.py#L1-L26 |
| <img src="/word_blocks/07x_more_sensors/07_optical_is_ambient_light.png" width="278"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/07_optical_is_ambient_light.py#L1-L11 |
| <img src="/word_blocks/07x_more_sensors/08_optical_get_ambient_light.png" width="169"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/08_optical_get_ambient_light.py#L1-L11 |
| <img src="/word_blocks/07x_more_sensors/09_device_get_type.png" width="161"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/07x_more_sensors/09_device_get_type.py#L1-L22 |

## Operators

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/08_operators/01_op_random.png" width="158"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/08_operators/01_op_random.py#L1-L4 |
| <img src="/word_blocks/08_operators/12_op_between.png" width="238"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/08_operators/12_op_between.py#L1-L2 |
| <img src="/word_blocks/08_operators/16_op_contains.png" width="192"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/08_operators/16_op_contains.py#L1-L5 |

## Hub to Hub Communication

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/09_hub_to_hub_communication/01_hub_transmit_message.png" width="306"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/09_hub_to_hub_communication/01_hub_transmit_message.py#L1-L8 |
| <img src="/word_blocks/09_hub_to_hub_communication/02_hub_on_message.png" width="263"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/09_hub_to_hub_communication/02_hub_on_message.py#L1-L11 |
| <img src="/word_blocks/09_hub_to_hub_communication/03_hub_get_message.png" width="216"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/09_hub_to_hub_communication/03_hub_get_message.py#L1-L6 |

## Debug

| Word block | Generated Python code (formatted and annotated) |
| -- | -- |
| <img src="/word_blocks/10_debug/01_device_get_data.png" width="265"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/10_debug/01_device_get_data.py#L1-L14 |
| <img src="/word_blocks/10_debug/02_device_set_data.png" width="207"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/10_debug/02_device_set_data.py#L1-L18 |
| <img src="/word_blocks/10_debug/03_device_set_mode.png" width="204"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/10_debug/03_device_set_mode.py#L1-L9 |
| <img src="/word_blocks/10_debug/04_device_apply_pwm.png" width="219"> | https://github.com/azzieg/mindstorms-inventor/blob/e6efa09fc7ff193947130f678f5a9b44236d78d7/word_blocks/10_debug/04_device_apply_pwm.py#L1-L9 |
