var status = {
  init: 0,
  finding: 1,
  finish: 2
};

var Postrow = React.createClass({
  render: function() {
    return (
        <div className='list-group-item row'>
                <div className='col-md-1'>
                <div><span className="badge">{this.props.post.rep_num}</span></div>
                </div>
                <div className='col-md-9'>
                    <a href={this.props.post.url_link} target="_blank">
                        <h4 className='list-group-item-head'>{this.props.post.title}</h4>
                    </a>
                    <p className='list-group-item-text'>{this.props.post.body}</p>
                </div>
                <div className='col-md-2'>
                <div><span className="glyphicon glyphicon-user" aria-hidden="true"></span> {this.props.post.author}</div>
                <div><span className="glyphicon glyphicon-time" aria-hidden="true"></span> {this.props.post.last_time}</div>
                </div>
                </div>
      );
  }
});


var Poststable = React.createClass({
  render: function() {
      if(this.props.status === status.init){
        return (<h2 className="text-center">请输入搜索条件</h2>);
        }
      else if(this.props.status === status.finding){
        return (<h2 className='text-center'>服务器正在搜索，请耐心等待</h2>);
        }
      else{
        if(this.props.posts.length === 0)
          return (<h2 className='text-center'>没有发现符合条件的帖子，请重新输入</h2>);
        else {
          var posts_list = this.props.posts.map(function(post) {
            return (<Postrow post={post} />);
          });
          return (
            <ul className='list-group'>
            {posts_list}
            </ul>
            );
        }
      } 
      }
});

var Searchbar = React.createClass({
  handleSubmit: function(e){
    e.preventDefault();
    var tieba_name = this.refs.tieba_name.getDOMNode().value.trim();
    var deepth = parseInt(this.refs.deepth.getDOMNode().value.trim());
    var rep_num = parseInt(this.refs.rep_num.getDOMNode().value.trim());
    var author = this.refs.author.getDOMNode().value.trim();
    this.props.onParaSubmit({tieba_name: tieba_name, author: author, rep_num: rep_num, deepth: deepth});
  },  
  render: function() {
    return (
      <div className='navbar navbar-inverse'>
            <div className="row">
                <div className='col-md-12'>
                    <h1 className="logotxt text-center text-primary">Tieba Dig</h1>
                    <h2 className="site-name text-primary text-center">a simple website for filtering tieba posts</h2>
                </div>
            </div>
            <div className="row">
            <div className="navbar-collapse collapse text-center">
                    <form className="navbar-form" role="form" onSubmit={this.handleSubmit}>
                        <div className='form-group'>
                            <input ref='tieba_name' type="text" placeholder='贴吧名' className='form-control' />
                        </div>
                        <div className='form-group'>
                            <input ref='deepth' type="text" placeholder='搜索页数' className='form-control' />
                        </div>
                        <div className='form-group'>
                            <input ref='rep_num' type="text" placeholder='最少回复量' className='form-control' />
                        </div>
                        <div className='form-group'>
                            <input ref='author' type="text" placeholder='作者(可省略)' className='form-control' />
                        </div>
                        <input type="submit" className='btn btn-success' value='GO'/>
                    </form>
                </div>
            </div>
          </div>
    );
  },
});

var Filtertable = React.createClass({
  handleParaSubmit: function(para) {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: para,
      success: function(posts) {
        console.log(posts);
        this.setState({posts: posts, status: status.finish});
      }.bind(this),
      error: function(xhr, status, err) {
          console.error(this.props.url, status, err.toString());
          }.bind(this)
    });
    this.setState({status: status.finding});
  },
  getInitialState: function() {
    return {posts: [], status: status.init};
  },
  render: function() {
    return (
      <div>
      // <Searchbar onParaSubmit={this.handleParaSubmit}/>
      <Poststable posts={this.state.posts} status={this.state.status}/>
      </div>
      );
  },
});


/*获取dom对象，传递属性，插入react组件*/
var content_dom = document.getElementById('content')
React.render(
  <Filtertable url='/search' blogs=content_dom.getAttribute('blogs') />,
  content_dom
  );
