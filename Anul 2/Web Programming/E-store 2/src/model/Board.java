package model;

import java.util.Arrays;
import java.util.Date;
import java.util.Random;

public class Board
{
    private int[][] board;
    public int x;
    public int y;
    private BoardPosition food;
    private Date startTime = new Date();

    public Board()
    {
        food=null;
        x = 11;
        y = 11;
        board = new int[x][y];
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                board[i][j] = 0; //empty piece
            }
        }
        Random rand = new Random();
        setObstaclePiece(new BoardPosition(rand.nextInt(x),rand.nextInt(y)));
        setObstaclePiece(new BoardPosition(rand.nextInt(x),rand.nextInt(y)));
        setObstaclePiece(new BoardPosition(rand.nextInt(x),rand.nextInt(y)));
    }

    public void setSnakePiece(BoardPosition position)
    {
        if(getPieceType(position)==2)
        {
            food=null;
        }
        board[position.getX()][position.getY()] = 1; //snake piece
    }

    public void setBlankPiece(BoardPosition position)
    {
        board[position.getX()][position.getY()] = 0;
    }

    public void setFoodPiece(BoardPosition position)
    {
        if (board[position.getX()][position.getY()] != 0)
            return;
        food=position;
        board[position.getX()][position.getY()] = 2; //food piece
    }

    public void setObstaclePiece(BoardPosition position)
    {
        if (board[position.getX()][position.getY()] != 0)
            return;
        board[position.getX()][position.getY()]= -1; //obstacle piece
    }

    public void ensureFood()
    {
        if(food!=null)
            return;

        Random rand = new Random();
        do {
            BoardPosition potentialFood = new BoardPosition(rand.nextInt(x),rand.nextInt(y));
            setFoodPiece(potentialFood);
        }while(getFood()==null);
    }

    public boolean validatePosition(BoardPosition position)
    {
        if(position.getX()<0 || position.getX()>=x || position.getY()<0 || position.getY()>=y)
            return false;

        return true;
    }

    public int getPieceType(BoardPosition position)
    {
        return board[position.getX()][position.getY()];
    }

    public int getX()
    {
        return x;
    }

    public void setX(int x)
    {
        this.x = x;
    }

    public int getY()
    {
        return y;
    }

    public void setY(int y)
    {
        this.y = y;
    }

    public int[][] getBoard() {
        return board;
    }

    public String getSerializedBoard()
    {
        String res =  Arrays.deepToString(board);
        return res;
    }

    public void setBoard(int[][] board) {
        this.board = board;
    }

    public BoardPosition getFood() {
        return food;
    }

    public int getFoodX()
    {
        if(food==null)
            return -1;
        return food.getX();
    }

    public int getFoodY()
    {
        if(food==null)
            return -1;
        return food.getY();
    }

    public void setFood(BoardPosition food) {
        this.food = food;
    }

    public Date getStartTime() {
        return startTime;
    }

    public void setStartTime(Date startTime) {
        this.startTime = startTime;
    }

}
