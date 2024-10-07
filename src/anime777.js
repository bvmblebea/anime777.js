class Anime777 {
	constructor() {
		this.api = "https://anime777.ru/api"
		this.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}
	}

	async loginWithConnectSid(connectSid) {
		this.connectSid = connectSid
		this.headers["cookie"] = `connect.sid=${this.connectSid}`
		const userInfo = await this.getCurrentUser()
		this.userId = userInfo.id
		this.userName = userInfo.name
		this.userAvatar = userInfo.photo
		return userInfo
	}

	async getCurrentUser() {
		const response = await fetch(
			`${this.api}/user/profile`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getReleased() {
		const response = await fetch(
			`${this.api}/enter/released`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUpdates() {
		const response = await fetch(
			`${this.api}/enter/updates`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async editProfilePrivateSettings(isClosed = false) {
		const response = await fetch(
			`${this.api}/user/closed`, {
				method: "PUT",
				body: JSON.stringify({
					closed: isClosed
				}),
				headers: this.headers
			})
		return response.json()
	}

	async changeNickname(nickname) {
		const response = await fetch(
			`${this.api}/user/nickname`, {
				method: "PUT",
				body: JSON.stringify({
					name: nickname
				}),
				headers: this.headers
			})
		return response.json()
	}

	async editProfile(
			photoUrl = null,
			sectionColor = null,
			textColor = null,
			themeColor = null,
			headerColor = null,
			linkColor = null,
			nicknameColor = null,
			profileHeader = null,
			profileBackground = null,
			auraColor = null,
			auraItem =  null) {
		const body = {}
		if (photoUrl) {
			body.photo = photoUrl
		}
		if (sectionColor) {
			body.section_color = sectionColor
		}
		if (textColor) {
			body.text_color = textColor
		}
		if (themeColor) {
			body.theme_color = themeColor
		}
		if (headerColor) {
			body.h_color = headerColor
		}
		if (linkColor) {
			body.a_color = linkColor
		}
		if (nicknameColor) {
			body.nickname_color = nicknameColor
		}
		if (profileHeader) {
			body.profile_header = profileHeader
		}
		if (profileBackground) {
			body.profile_bg = profileBackground
		}
		if (auraColor) {
			body.aura_color = auraColor
		}
		if (auraItem) {
			body.aura_item = auraItem
		}
		const response = await fetch(
			`${this.api}/user`, {
				method: "PUT",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.json()
	}

	async getFriends() {
		const response = await fetch(
			`${this.api}/user/profile/friends`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getSentComments() {
		const response = await fetch(
			`${this.api}/user/profile/comments`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getReferrals() {
		const response = await fetch(
			`${this.api}/user/profile/referrals`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getFavorites() {
		const response = await fetch(
			`${this.api}/user/profile/favs`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getIndexData() {
		const response = await fetch(
			`${this.api}/indexdata`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCatalog(sort = null, year = null, page = 1, status = null) {
		const body = {}
		if (sort) {
			body.sort = sort
		}
		if (year) {
			body.year = year
		}
		if (page) {
			body.page = page
		}
		if (status) {
			body.status = status
		}
		const response = await fetch(
			`${this.api}/api/catalog"`, {
				method: "POST",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.json()
	}

	async getNeedFriends(page = 1) {
		const response = await fetch(
			`${this.api}/need-friends?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUserProfile(userId) {
		const response = await fetch(
			`${this.api}/users/${userId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async friendlyCheck(userId) {
		const response = await fetch(
			`${this.api}/user/friendly/check`, {
				method: "POST",
				body: JSON.stringify({
					user_id: userId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getWatchInfo(watchId) {
		const response = await fetch(
			`${this.api}/watch?id=${watchId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getWatchComments(watchId, page = 1) {
		const response = await fetch(
			`${this.api}/watch?id=${watchId}&page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async sendComment(text, id, parentId = null) {
		const body = {
			id: id,
			user_id: this.userId,
			user_name: this.userName,
			user_avatar: this.userAvatar,
			user_group: 1,
			text: text,
			data: Math.floor(Date.now() / 1000) * 1000
		}
		if (parentId) {
			body.parent_id = parentId
		}
		const response = await fetch(
			`${this.api}/comments"`, {
				method: "POST",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.json()
	}

	async getSchedule() {
		const response = await fetch(
			`${this.api}/schedule`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getBlogs(page = 1) {
		const response = await fetch(
			`${this.api}/blogs?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getBlogArticles(blogId, page = 1) {
		const response = await fetch(
			`${this.api}/blogs/${blogId}/articles?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getBlogArticle(blogId, articleId) {
		const response = await fetch(
			`${this.api}/blogs/${blogId}/${articleId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getArticleComments(blogId, articleId, page = 1) {
		const response = await fetch(
			`${this.api}/blogs/${blogId}-${articleId}&page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async putReaction(id, reaction) {
		const response = await fetch(
			`${this.api}/reactions`, {
				method: "POST",
				body: JSON.stringify({
					id: id,
					reaction: reaction
				}),
				headers: this.headers
			})
		return response.text()
	}

	async getComments(page = null) {
		let url = `${this.api}/comments-page`
		if (page) {
			url += `?page=${page}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getUsers(page = 1) {
		const response = await fetch(
			`${this.api}/users?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getArticles() {
		const response = await fetch(
			`${this.api}/articles`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async sendPm(userId, text) {
		const response = await fetch(
			`${this.api}/user/pm`, {
				method: "POST",
				body: JSON.stringify({
					to: userId,
					text: text
				}),
				headers: this.headers
			})
		return response.json()
	}

	async sendFriendRequest(userId) {
		const response = await fetch(
			`${this.api}/user/friendly`, {
				method: "POST",
				body: JSON.stringify({
					to: userId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async getRooms() {
		const response = await fetch(
			`${this.api}/rooms`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getStreams() {
		const response = await fetch(
			`${this.api}/tv`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getPopular() {
		const response = await fetch(
			`${this.api}/popular`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getBattlesToday() {
		const response = await fetch(
			`${this.api}/battles/today`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCharacters(page = 1) {
		const response = await fetch(
			`${this.api}/chars?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGames(page = 1) {
		const response = await fetch(
			`${this.api}/games?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getGameInfo(gameId) {
		const response = await fetch(
			`${this.api}/games/${game_id}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCinema(page = 1) {
		const response = await fetch(
			`${this.api}/cinema?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getCinemaInfo(cinemaId) {
		const response = await fetch(
			`${this.api}/cinema?id=${cinemaId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getRandomAnime() {
		const response = await fetch(
			`${this.api}/rand`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getRanobes(page = 1) {
		const response = await fetch(
			`${this.api}/ranobes?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getRanobeInfo(ranobeId) {
		const response = await fetch(
			`${this.api}/ranobes/${ranobeId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getComics(page = 1) {
		const response = await fetch(
			`${this.api}/comics?page=${page}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getComicsInfo(comicsId) {
		const response = await fetch(
			`${this.api}/comics/${comicsId}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getNotifications() {
		const response = await fetch(
			`${this.api}/user/notifications`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getInventory() {
		const response = await fetch(
			`${this.api}/items/store`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async buyItem(itemType, itemId) {
		const response = await fetch(
			`${this.api}/items/buy`, {
				method: "POST",
				body: JSON.stringify({
					type: itemType,
					id: itemId
				}),
				headers: this.headers
			})
		return response.json()
	}

	async buyRandomItem() {
		const response = await fetch(
			`${this.api}/items/random`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getInbox() {
		const response = await fetch(
			`${this.api}/user/profile/pms`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async editAbout(
			realName = null,
			age = null,
			gender = null,
			country = null,
			city = null,
			contacts = null,
			about = null) {
		const body = {}
		if (realName) {
			body.real_name = realName
		}
		if (age) {
			body.age = age
		}
		if (gender) {
			body.gender = gender
		}
		if (country) {
			body.country = country
		}
		if (city) {
			body.city = city
		}
		if (contacts) {
			body.contacts = contacts
		}
		if (about) {
			body.about = about
		}
		const response = await fetch(
			`${this.api}/user/about`, {
				method: "PUT",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.json()
	}
}

module.exports = {Anime777}
