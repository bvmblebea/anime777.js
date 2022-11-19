import requests
from time import time

class Anime777:
	def __init__(self) -> None:
		self.api = "https://anime777.ru/api"
		self.headers = {
			"connection": "keep-alive",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}
		self.user_id = None
		self.username = None
		self.user_avatar = None
		self.connect_sid = None

	def login_with_connect_sid(self, connect_sid: str) -> dict:
		self.connect_sid = connect_sid
		self.headers["cookie"] = f"connect.sid={self.connect_sid}"
		response = self.get_current_user()
		self.user_id = response["id"]
		self.username = response["name"]
		self.user_avatar = response["photo"]
		return response

	def get_current_user(self) -> dict:
		return requests.get(
			f"{self.api}/user/profile",
			headers=self.headers).json()

	def get_released(self) -> dict:
		return requests.get(
			f"{self.api}/enter/released",
			headers=self.headers).json()

	def get_updates(self) -> dict:
		return requests.get(
			f"{self.api}/enter/updates",
			headers=self.headers).json()

	def open_profile(self) -> dict:
		data = {
			"closed": False
		}
		return requests.put(
			f"{self.api}/user/closed",
			data=data,
			headers=self.headers).json()

	def close_profile(self) -> dict:
		data = {
			"closed": True
		}
		return requests.put(
			f"{self.api}/user/closed",
			data=data,
			headers=self.headers).json()

	def change_nickname(self, nickname: str) -> dict:
		data = {
			"name": nickname
		}
		return requests.post(
			f"{self.api}/user/nickname",
			data=data,
			headers=self.headers).json()

	def edit_profile(
			self,
			photo_url: str = None,
			section_color: str = None,
			text_color: str = None,
			theme_color: str = "dark",
			header_color: str = None,
			link_color: str = None,
			nickname_color: str = None,
			profile_header: str = None,
			profile_background: str = None,
			aura_color: str = None,
			aura_item: str = None) -> dict:
		data = {}
		if photo_url:
			data["photo"] = photo_url
		if section_color:
			data["section_color"] = section_color
		if text_color:
			data["text_color"] = text_color
		if theme_color:
			data["theme_color"] = theme_color
		if header_color:
			data["h_color"] = header_color
		if link_color:
			data["a_color"] = link_color
		if nickname_color:
			data["nickname_color"] = nickname_color
		if profile_header:
			data["profile_header"] = profile_header
		if profile_background:
			data["profile_bg"] = profile_background
		if aura_color:
			data["aura_color"] = aura_color
		if aura_item:
			data["aura_item"] = aura_item
		return requests.put(
			f"{self.api}/user",
			json=data,
			headers=self.headers).json()

	def get_friends(self) -> dict:
		return requests.get(
			f"{self.api}/user/profile/friends",
			headers=self.headers).json()

	def get_sent_comments(self) -> dict:
		return requests.get(
			f"{self.api}/user/profile/comments",
			headers=self.headers).json()

	def get_referrals(self) -> dict:
		return requests.get(
			f"{self.api}/user/profile/referrals",
			headers=self.headers).json()

	def get_favorites(self) -> dict:
		return requests.get(
			f"{self.api}/user/profile/favs",
			headers=self.headers).json()

	def get_index_data(self) -> dict:
		return requests.get(
			f"{self.api}/indexdata",
			headers=self.headers).json()

	def get_catalog(
			self,
			sort: str = None,
			year: int = None,
			page: int = 1,
			status: str = None) -> dict:
		data = {}
		if year:
			data["year"] = year
		if page:
			data["page"] = page
		if status:
			data["status"] = status
		if sort:
			data["sort"] = sort
		return requests.post(
			f"{self.api}/api/catalog",
			data=data,
			headers=self.headers).json()

	def get_need_friends(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/need-friends?page={page}",
			headers=self.headers).json()

	def get_user_profile(self, user_id: str) -> dict:
		return requests.get(
			f"{self.api}/users/{user_id}",
			headers=self.headers).json()

	def friendly_check(self, user_id: str) -> dict:
		data = {
			"user_id": user_id
		}
		return requests.post(
			f"{self.api}/user/friendly/check",
			data=data,
			headers=self.headers).json()

	def get_watch_info(self, watch_id: str) -> dict:
		return requests.get(
			f"{self.api}/watch?id={watch_id}",
			headers=self.headers).json()

	def get_watch_comments(self, watch_id: str, page: int  = 1) -> dict:
		return requests.get(
			f"{self.api}/comments?id={watch_id}&page={page}",
			headers=self.headers).json()

	def send_comment(
			self,
			text: str,	
			id: str,
			parent_id: str = None) -> dict:
		data = {
			"id": id,
			"user_id": self.user_id,
			"user_name": self.username,
			"user_avatar": self.user_avatar,
			"user_group": 1,
			"text": text,
			"date": int(time() * 1000)
		}
		if parent_id:
			data["parent_id"] = parent_id
		return requests.post(
			f"{self.api}/comments",
			data=data,
			headers=self.headers).json()

	def delete_comment(self, comment_id: str) -> dict:
		return requests.delete(
			f"{self.api}/comments?id={comment_id}&user_id={self.user_id}",
			headers=self.headers).text

	def get_schedule(self) -> dict:
		return requests.get(
			f"{self.api}/schedule",
			headers=self.headers).json()

	def get_blogs(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/blogs?page={page}",
			headers=self.headers).json()

	def get_blog_articles(self, blog_id: str, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/blogs/{blog_id}/articles?page={page}",
			headers=self.headers).json()

	def get_blog_article(self, blog_id: str, article_id: str) -> dict:
		return requests.get(
			f"{self.api}/blogs/{blog_id}/{article_id}",
			headers=self.headers).json()

	def get_article_comments(
			self,
			blog_id: str,
			article_id: str,
			page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/comments?id={blog_id}-{article_id}&page={page}",
			headers=self.headers).json()

	def put_reaction(self, id: str, reaction: str) -> dict:
		data = {
			"id": id,
			"reaction": reaction
		}
		return requests.post(
			f"{self.api}/reactions",
			data=data,
			headers=self.headers).text

	def get_comments(self, page: int = None) -> dict:
		url = f"{self.api}/comments-page"
		if page:
			url += f"?page={page}"
		return requests.get(
			url, headers=self.headers).json()

	def get_users(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/users?page={page}",
			headers=self.headers).json()

	def get_articles(self) -> dict:
		return requests.get(
			f"{self.api}/articles",
			headers=self.headers).json()

	def send_pm(self, user_id: str, text: str) -> dict:
		data = {
			"to": user_id,
			"text": text
		}
		return requests.post(
			f"{self.api}/user/pm",
			data=data,
			headers=self.headers).json()

	def send_friend_request(self, user_id: str) -> dict:
		data = {
			"to": user_id
		}
		return requests.post(
			f"{self.api}/user/friendly",
			data=data,
			headers=self.headers).json()

	def cancel_friend_request(self, user_id: str) -> dict:
		return requests.delete(
			f"{self.api}/user/friendly?id={user_id}",
			headers=self.headers).json()

	def get_rooms(self) -> dict:
		return requests.get(
			f"{self.api}/rooms",
			headers=self.headers).json()

	def get_partners_list(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/partnerslist?page={page}",
			headers=self.headers).json()

	def check_partners_stats(self, channel_name: str) -> dict:
		data = {
			"channel_name": channel_name
		}
		return requests.post(
			f"{self.api}/partners/stats",
			data=data,
			headers=self.headers).json()

	def get_streams(self) -> dict:
		return requests.get(
			f"{self.api}/tv",
			headers=self.headers).json()

	def get_popular(self) -> dict:
		return requests.get(
			f"{self.api}/popular",
			headers=self.headers).json()

	def get_quiz(self, type: str = "anime") -> dict:
		return requests.get(
			f"{self.api}/quiz?type={type}",
			headers=self.headers).json()

	def sent_quiz_result(self, result: str) -> dict:
		data = {
			"result": result
		}
		return requests.post(
			f"{self.api}/quiz",
			data=data,
			headers=self.headers).json()

	def get_battles_today(self) -> dict:
		return requests.get(
			f"{self.api}/battles/today",
			headers=self.headers).json()

	def get_characters(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/chars?page={page}",
			headers=self.headers).json()

	def get_character_info(self, character_id: int, character_link: str) -> dict:
		data = {
			"id": character_id,
			"link": character_link
		}
		return requests.post(
			f"{self.api}/charinfo",
			data=data,
			headers=self.headers).json()

	def get_games(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/games?page={page}",
			headers=self.headers).json()

	def get_game_info(self, game_id: int) -> dict:
		return requests.get(
			f"{self.api}/games/{game_id}",
			headers=self.headers).json()

	def get_game_comments(self, game_id: int, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/comments?id=games-{game_id}&page={page}",
			headers=self.headers).json()

	def get_cinema(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/cinema?page={page}",
			headers=self.headers).json()

	def get_cinema_info(self, cinema_id: str) -> dict:
		return requests.get(
			f"{self.api}/cinema?id={cinema_id}",
			headers=self.headers).json()

	def create_cinema(self, watch_id: str, is_hidden: bool = False) -> dict:
		data = {
			"id": watch_id,
			"user_id": self.user_id,
			"user_group": 1,
			"hidden": is_hidden
		}
		return requests.post(
			f"{self.api}/cinema",
			headers=self.headers).json()

	def get_random_anime(self) -> dict:
		return requests.get(
			f"{self.api}/rand",
			headers=self.headers).json()

	def get_ranobes(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/ranobes?page={page}",
			headers=self.headers).json()

	def get_ranobe_info(self, ranobe_id: int) -> dict:
		return requests.get(
			f"{self.api}/ranobes/{ranobe_id}",
			headers=self.headers).json()

	def get_ranobe_comments(self, ranobe_id: int, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/comments?id=ranobes-{ranobe_id}&page={page}",
			headers=self.headers).json()

	def get_comics(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/comics?page={page}",
			headers=self.headers).json()

	def get_comics_info(self, comics_id: int) -> dict:
		return requests.get(
			f"{self.api}/comics/{comics_id}",
			headers=self.headers).json()

	def get_comics_comments(self, comics_id: int, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/comments?id=comics-{comics_id}&page={page}",
			headers=self.headers).json()

	def get_notifications(self) -> dict:
		return requests.get(
			f"{self.api}/user/notifications",
			headers=self.headers).json()

	def get_inventory(self) -> dict:
		return requests.get(
			f"{self.api}/items/store",
			headers=self.headers).json()

	def buy_item(self, item_type: str, item_id: int) -> dict:
		data = {
			"type": item_type,
			"id": item_id
		}
		return requests.post(
			f"{self.api}/items/buy",
			data=data,
			headers=self.headers).json()

	def buy_random_item(self) -> dict:
		return requests.get(
			f"{self.api}/items/random",
			headers=self.headers).json()

	def get_inbox(self) -> dict:
		return requests.get(
			f"{self.api}/user/profile/pms",
			headers=self.headers).json()

	def redeem_promo_ccode(self, promo_code: str) -> dict:
		data = {
			"code": promo_code
		}
		return requests.post(
			f"{self.api}/promocodes",
			data=data,
			headers=self.headers).json()

	def edit_about(
			self,
			real_name: str = None,
			age: int = None,
			gender: str = "male",
			country: str = None,
			city: str = None,
			contacts: str = None,
			about: str = None) -> dict:
		data = {}
		if real_name:
			data["realname"] = real_name
		if age:
			data["age"] = age
		if gender:
			data["gender"] = gender
		if country:
			data["country"] = country
		if city:
			data["city"] = city
		if contacts:
			data["contacts"] = contacts
		if about:
			data["about"] = about
		return requests.post(
			f"{self.api}/user/about",
			data=data,
			headers=self.headers).json()
