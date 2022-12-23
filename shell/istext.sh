is_text()
{
    out=`file $1`
    if [[ $out =~ "text" ]]; then
        echo "0"
    else
        echo "1"
    fi
}
