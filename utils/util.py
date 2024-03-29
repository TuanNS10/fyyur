from datetime import datetime

import dateutil.parser
import babel
from models import Show
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format="EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format="EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')

def search(db_class, skey):
    data = []
    results = db.session.query(db_class).filter(db_class.name.ilike(f'%{skey}%') | 
                                                db_class.city.ilike(f'%{skey}%') | 
                                                db_class.state.ilike(f'%{skey}%')).all()
    for result in results:
        data.append({
            "id": result.id,
            "name": result.name,
            "num_upcoming_shows": len(db.session.query(Show).filter(Show.venue_id == result.id)
                                       .filter(Show.start_time > datetime.now()).all()),
        })
    results_data = {
        "count": len(results),
        "data": data
    }
    return results_data
