package iscas.nfs.dao;

import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

/**
 * @private value Connection and Statement and a DataBase
 * @function instance is the interface for external invoke
 * @function getConnection() and getStatement() is used to get the private value
 * @author Caowenlong Date 2017/6/8
 * @description this class use to build the connection with database
 * @investigator
 * @more reference:
 *       https://stackoverflow.com/questions/21955256/manipulating-an-
 *       access-database-from-java-without-odbc
 **/
public class DataBase {
	private static Connection con = null; // Declare the db connection
	private static Statement stat = null; // Declare the statement
	private static DataBase dataBase = null;

	/**
	 * @param null
	 * @author caowenlong 2017/6/8
	 * @return DataBase
	 * */
	public static DataBase instance() {
		if (dataBase == null) {
			try {
				/* load the properties from the .properties file */
				Properties config = ProperityInfo.getProperties();
				String url = config.getProperty("url");
				String username = config.getProperty("username");
				String password = config.getProperty("password");

				// 此处是为了留着将来给非access使用的
				// Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");// add the DB
				// driver
				dataBase = new DataBase();
				dataBase.con = DriverManager.getConnection(url, username,
						password);// building the connection

				dataBase.stat = con.createStatement();// get the statement

			} catch (Exception e) {

				throw new ExceptionInInitializerError(e);
			}

			return dataBase;
		} else {
			return dataBase;
		}

	}

	public Connection getConnection() {
		if (dataBase == null) {
			return DataBase.instance().getConnection();
		} else {
			return con;
		}

	}

	public Statement getStatement() {
		if (dataBase == null) {
			return DataBase.instance().getStatement();
		} else {
			return stat;
		}
	}

	public static List<String> getAllTableNames(Connection con, String dbname, String username) {

		List<String> tableNames = new ArrayList<String>();
		if (con != null) {
			System.out.println("connection not null");
			try {
				DatabaseMetaData dbmd = con.getMetaData();
				// 表名列表
				ResultSet rest = dbmd.getTables(dbname, " ", " ",
						new String[] { "TABLE" });
				// 输出 table_name
				while (rest.next()) {
					String tableSchem = rest.getString("TABLE_SCHEM");
					if (username.equalsIgnoreCase(tableSchem)) {
						tableNames.add(rest.getString("TABLE_NAME"));
					}
				}
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		return tableNames;
	}

	public static void main(String[] args) {
//		for (int i = 0; i < 10; i++) {
//			System.out.println("Test time:" + (i + 1));
//			System.out.println("this is Connection "
//					+ DataBase.instance().getConnection());
//			System.out.println("this is Statement "
//					+ DataBase.instance().getStatement());
//			System.out.println();
//		}
		DataBase db = new DataBase();
		Connection connection = db.getConnection();
		List<String> aList = DataBase.getAllTableNames(connection, "", "");
		for(String table: aList)
		{
			System.out.println(table);
		}
		System.out.println("---------------");

	} 

}
