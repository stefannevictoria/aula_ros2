import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/inteli/Documentos/codigos/2026/M06-Inteli2026/aulas/aula_ros2/install/turtle_circle'
