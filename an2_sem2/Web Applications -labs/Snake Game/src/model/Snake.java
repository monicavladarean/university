package model;

import java.util.ArrayList;
import java.util.List;

public class Snake {
    private ArrayList<BoardPosition> snakePositions;

    public Snake() {
        this.snakePositions = new ArrayList<BoardPosition>();
    }

    public BoardPosition getHead() {
        return snakePositions.get(0);
    }

    public void addHead(BoardPosition boardPosition, Board tabla) {
        snakePositions.add(0, boardPosition);
        tabla.setSnakePiece(boardPosition);
    }

    public BoardPosition getTail() {
        return snakePositions.get(snakePositions.size() - 1);
    }

    public void cutTail(Board tabla) {
        BoardPosition tail = getTail();
        snakePositions.remove(snakePositions.size() - 1);
        tabla.setBlankPiece(tail);
    }

    public void addTail(BoardPosition boardPosition) {
        snakePositions.add(boardPosition);
    }

    public boolean isHead(BoardPosition position)
    {
        if(position.getX()==getHead().getX() && position.getY()==getHead().getY())
            return true;
        return false;
    }

    public boolean move(Direction direction, Board tabla) {
        BoardPosition head = getHead();
        BoardPosition newHead = new BoardPosition(head.getX() + direction.x, head.getY() + direction.y);
        if (tabla.validatePosition(newHead)==false || tabla.getPieceType(newHead)==-1 || tabla.getPieceType(newHead)==1)
            return false;
        boolean grow = tabla.getPieceType(newHead)==2;
        addHead(newHead, tabla);
        if(!grow)
            cutTail(tabla);
        tabla.ensureFood();
        return true;
    }
}
