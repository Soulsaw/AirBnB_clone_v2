# puppet configuration

#Installation of nginx
package {'nginx':
    ensure          => installed,
    name            => 'nginx',
    provider        => apt,
    install_options => '-y',
    }
$data = '/data/'
$data_stat = '/data/web_static/'
$data_stat_rel = '/data/web_static/releases/'
$data_stat_shar = '/data/web_static/shared/'
$data_stat_rel_test = '/data/web_static/releases/test/'
$html_file = '/data/web_static/releases/test/index.html'
$sl_name =  '/data/web_static/current'

# Create the different folder
exec {'create /data/':
    command => "mkdir -p ${data}",
    creates => $data,
    cwd     => '/',
    path    => ['/usr/bin', '/usr/sbin'],
    }
exec {'create /data/web_static':
    command => "mkdir -p ${data_stat}",
    creates => $data_stat,
    cwd     => '/',
    path    => ['/usr/bin', '/usr/sbin'],
    }
exec {'create /data/web_static/releases':
    command => "mkdir -p ${data_stat_rel}",
    creates => $data_stat_rel,
    cwd     => '/',
    path    => ['/usr/bin', '/usr/sbin'],
    }
exec {'create /data/web_static/shared':
    command => "mkdir -p ${data_stat_shar}",
    creates => $data_stat_shar,
    cwd     => '/',
    path    => ['/usr/bin', '/usr/sbin'],
    }
exec {'create /data/web_static/releases/test':
    command => "mkdir -p ${data_stat_rel_test}",
    creates => $data_stat_rel_test,
    cwd     => '/',
    path    => ['/usr/bin', '/usr/sbin'],
    }
# create the html content
$content = "<html>
<head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
file {'create the /data/web_static/releases/test/index.html file':
    ensure  => present,
    path    => $html_file,
    content => $content,
    }
file {'create symbolic link':
    ensure => link,
    name   => $sl_name,
    target => $data_stat_rel_test,
}
file {'Give owner to ubuntu':
    ensure => directory,
    name   => $data,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    }
$config_file = '/etc/nginx/sites-enabled/default'
$new_string = "server_name _;\n\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n"
exec {'Configure the nginx server':
    command => "sed -i 's|server_name _;|${new_string}|' ${config_file}",
    creates => $config_file,
    cwd     => '/',
    path    => ['/usr/bin', '/usr/sbin'],
    }
