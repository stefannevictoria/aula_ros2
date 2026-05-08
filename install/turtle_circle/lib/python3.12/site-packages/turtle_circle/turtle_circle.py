import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleCircle(Node):
    def __init__(self):
        super().__init__('turtle_circle')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10) # A fila é de no máximo 10 mensagens
        timer_period = 0.1  # setando o período do timer para 0.1 segundos (10 Hz)
        self.timer = self.create_timer(timer_period, self.timer_callback) # Cria um timer que chama a função timer_callback a cada 0.1 segundos para publicar mensagens de velocidade e fazer a tartaruga se mover em um círculo

    def timer_callback(self):
        msg = Twist() # Cria uma mensagem do tipo Twist e depois seta a velocidade linear e angular para fazer a tartaruga se mover em um círculo
        msg.linear.x = 2.0  # Seta a velocidade linear para 2.0 m/s
        msg.angular.z = 2.0  # Seta a velocidade angular para 2.0 rad/s
        self.publisher_.publish(msg) # Publica a mensagem no tópico 'turtle1/cmd_vel' para controlar a tartaruga (pode setar parâmetros para o nó)


def main(args=None):
    rclpy.init(args=args) # Inicializa o ROS 2
    turtle_circle = TurtleCircle() # Cria uma instância do nó TurtleCircle
    rclpy.spin(turtle_circle) # Mantém o nó rodando para que ele possa publicar mensagens continuamente
    turtle_circle.destroy_node() # Destrói o nó quando ele for encerrado
    rclpy.shutdown() # Encerra o ROS 2

if __name__ == '__main__':
    main() # Chama a função principal para iniciar o nó