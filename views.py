def hello_view(name, hostname) -> str:
    return f"""
        <h1>Hello, {name}!</h1> 
        <b>Hostname:</b> {hostname} <br>
        """


def stat_view(date, user_agent) -> str:
    return f"""
        <b>Datetime</b>: {date} <br>
        <b>Client User-Agent</b>: {user_agent}
        """