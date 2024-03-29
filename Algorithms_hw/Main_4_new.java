package Algorithms_hw;

class RedBlackTree {
    class Node {
        int value;
        boolean isRed;
        Node left;
        Node right;

        Node(int value) {
            this.value = value;
            this.isRed = true; // Новая нода всегда красная
        }
    }

    Node root;

    boolean insert(int value) {
        if (root == null) {
            root = new Node(value);
            root.isRed = false; // Корень дерева всегда черный
            return true;
        } else {
            Node parent = null;
            Node node = root;
            while (node != null) {
                if (node.value == value) {
                    return false; // Не добавляем дубликаты
                }
                parent = node;
                if (node.value < value) {
                    node = node.right;
                } else {
                    node = node.left;
                }
            }
            // Создаем новую красную ноду
            Node newNode = new Node(value);
            if (parent.value < value) {
                parent.right = newNode;
            } else {
                parent.left = newNode;
            }
            // Выполняем балансировку
            balanceAfterInsert(newNode, parent);
            return true;
        }
    }

    void balanceAfterInsert(Node node, Node parent) {
        // Пока родитель нода красная, выполняем балансировку
        while (parent != null && parent.isRed) {
            Node grandParent = findGrandParent(node, parent);
            Node uncle = findUncle(node, parent, grandParent);

            if (uncle != null && uncle.isRed) {
                // Дядя нода тоже красный - меняем цвета
                parent.isRed = false;
                uncle.isRed = false;
                grandParent.isRed = true;
                // Переходим к балансировке у дедушки
                node = grandParent;
                parent = findParent(node);
            } else {
                if (parent == grandParent.left) {
                    if (node == parent.right) {
                        // Левый поворот
                        rotateLeft(parent);
                        // Обновляем ссылки
                        node = parent;
                        parent = findParent(node);
                    }
                    // Правый поворот
                    rotateRight(grandParent);
                    // Меняем цвета
                    grandParent.isRed = true;
                    parent.isRed = false;
                } else {
                    if (node == parent.left) {
                        // Правый поворот
                        rotateRight(parent);
                        // Обновляем ссылки
                        node = parent;
                        parent = findParent(node);
                    }
                    // Левый поворот
                    rotateLeft(grandParent);
                    // Меняем цвета
                    grandParent.isRed = true;
                    parent.isRed = false;
                }
            }
        }
        // Корень дерева всегда черный
        root.isRed = false;
    }

    Node findParent(Node node) {
        if (node == null || node == root) {
            return null;
        }
        Node parent = root;
        while (parent != null) {
            if (parent.left == node || parent.right == node) {
                return parent;
            }
            if (parent.value < node.value) {
                parent = parent.right;
            } else {
                parent = parent.left;
            }
        }
        return null;
    }

    Node findGrandParent(Node node, Node parent) {
        Node grandParent = null;
        if (parent != null) {
            grandParent = findParent(parent);
        }
        return grandParent;
    }

    Node findUncle(Node node, Node parent, Node grandParent) {
        if (grandParent != null) {
            if (grandParent.left == parent) {
                return grandParent.right;
            } else {
                return grandParent.left;
            }
        }
        return null;
    }

    void rotateLeft(Node node) {
        if (node != null) {
            Node rightChild = node.right;
            if (rightChild != null) {
                node.right = rightChild.left;
                rightChild.left = node;
                if (node == root) {
                    root = rightChild;
                }
            }
        }
    }

    void rotateRight(Node node) {
        if (node != null) {
            Node leftChild = node.left;
            if (leftChild != null) {
                node.left = leftChild.right;
                leftChild.right = node;
                if (node == root) {
                    root = leftChild;
                }
            }
        }
    }

    boolean find(int value) {
        Node node = root;
        while (node != null) {
            if (node.value == value) {
                return true;
            }
            if (node.value < value) {
                node = node.right;
            } else {
                node = node.left;
            }
        }
        return false;
    }
}

public class Main_4_new {
    public static void main(String[] args) {
        RedBlackTree tree = new RedBlackTree();

        tree.insert(5);
        tree.insert(3);
        tree.insert(7);
        tree.insert(2);
        tree.insert(4);
        tree.insert(6);
        tree.insert(8);

        System.out.println(tree.find(8));
        System.out.println(tree.find(10));
    }
}

