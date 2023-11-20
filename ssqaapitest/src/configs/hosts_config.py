API_HOSTS = {
    'test': 'http://pidnebesnyi.local/wp-json/wc/v3/',
    'dev': '',
    'prod': 'http://pidnebesnyi.local/wp-json/wc/v3/'
}

WOO_API_HOSTS = {
    'test': 'http://pidnebesnyi.local',
    'dev': '',
    'prod': 'http://pidnebesnyi.local/wp-json/wc/v3/'
}

DB_HOSTS = {
    'machine1': {
        'test': {
            'host': 'localhost',
            'database': 'local',
            'table_prefix': 'wp_',
            'socket': '/Users/koshevarov.roma/Library/Application Support/Local/run/wVkmYuBvK/mysql/mysqld.sock',
            'port': 3306
        },
        'dev': {
            'host': 'localhost',
            'database': 'local',
            'table_prefix': 'wp_',
            'socket': '/Users/koshevarov.roma/Library/Application Support/Local/run/wVkmYuBvK/mysql/mysqld.sock',
            'port': 3306
        },
        'prod': {
            'host': 'localhost',
            'database': 'local',
            'table_prefix': 'wp_',
            'socket': '/Users/koshevarov.roma/Library/Application Support/Local/run/wVkmYuBvK/mysql/mysqld.sock',
            'port': 3306
        }
    },
    'docker': {
        'test': {
            'host': 'host.docker.internal',
            'database': 'local',
            'table_prefix': 'wp_',
            'socket': None,
            'port': 3306
        },
        'dev': {
            'host': 'localhost',
            'database': 'local',
            'table_prefix': 'wp_',
            'socket': '/Users/koshevarov.roma/Library/Application Support/Local/run/wVkmYuBvK/mysql/mysqld.sock',
            'port': 3306
        },
        'prod': {
            'host': 'localhost',
            'database': 'local',
            'table_prefix': 'wp_',
            'socket': '/Users/koshevarov.roma/Library/Application Support/Local/run/wVkmYuBvK/mysql/mysqld.sock',
            'port': 3306
        }
    },

}