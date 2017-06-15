package iscas.nfs.dao;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class ProperityInfo {
	private static Properties config = null;
	public static final String DATABASE_FILENAME = "DB.properties";

	/**
	 * @param null
	 * @return Properties from the .properties
	 * @Discribe 获取.Properties(配置文件) 信息,相当于一个数据对象存储静态数据
	 */
	public static Properties getProperties() {
		if (config == null) {
			config = new Properties();
			InputStream in = ProperityInfo.class.getClassLoader()
					.getResourceAsStream(DATABASE_FILENAME);
			try {
				config.load(in);
				System.out.println(" Config load success!");
				return config;
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			return config;
		}
		return null;
	}
}
